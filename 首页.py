import streamlit as st
from datetime import time, date
from PIL import Image
import io
import streamlit as st
import pandas as pd
import random
st.set_page_config(
    page_title="页面整合",
    page_icon="📄",
    layout="wide"
)

st.title("机器学习项目大致流程")
# 创建选项卡
tab1, tab2, tab3,tab4 = st.tabs(["个人简历生成器", "南宁美食", "视频播放器","数字档案"])
with tab1:   
    # 添加标题和描述
    st.title("🎨个人简历生成器")
    st.caption("使用Streamlit创建您的个性化简历")
    ##初始化session_state（存储上传的图片）
    if 'uploaded_image' not in st.session_state:
        st.session_state.uploaded_image = None
    if 'languages' not in st.session_state:
        st.session_state.languages = ["中文"]  # 设置默认语言
    if 'skills' not in st.session_state:
        st.session_state.skills = []
    if 'bio' not in st.session_state:  # 添加个人简介的初始化
        st.session_state.bio = None    
    # 创建两列布局
    if 'certificates' not in st.session_state:
        st.session_state.certificates = ""
    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.header("个人信息表单", divider="blue")
        
        # 基本信息部分
        st.subheader("基本信息")
        
        # 姓名和职位布局 - 已去除下拉效果
        st.text_input("姓名", key="name")
        st.selectbox("职位",[" ","工人👨‍🏭","组长","厨师长", "厂长", "CEO"],key="position")      
        phone_types = [" ","水果16", "OPPO A5", "菠萝手机","小米15pro", "其他"]
        phone_type = st.selectbox("电话", phone_types, key="phone_type")
        
        # 当选择"其他"时，显示自定义输入框
        if phone_type == "其他":
            custom_phone = st.text_input("请输入您的电话", key="custom_phone")        
            if custom_phone:
                phone_type = custom_phone
        
        email = st.text_input("邮箱", key="email")
        st.date_input("出生日期", value=date(2015, 6, 13), key="birth_date")    
        # 性别和学历布局
        gender = st.radio("性别", ["男", "女", "其他物种"], horizontal=True, key="gender")
        st.subheader("在校经历", divider="blue")
        education = st.selectbox("学历", [" ","小学","初中","高中", "大专", "本科", "硕士", "博士"], key="education")
        st.text_input("毕业院校",placeholder="输入院校名称...", key="school")
        
        # 工作经验和期望薪资
        
        st.session_state.languages = st.multiselect(
            "语言能力",
            options=["中文", "英语四级", "英语六级", "德语", "日语", "法语", "俄罗斯语"],
            default=st.session_state.languages,
            placeholder="请选择你的语言...", 
            key="languages_selector"
        )
        
        st.session_state.skills = st.multiselect(
            "技能（可多选）",
            options=["Python", "C++","Java", "JavaScript", "HTML/CSS", "SQL", "数据分析", "深度学习", "网络安全","后勤工程"],
            default=st.session_state.skills,
            placeholder="请选择你的技能...",
            key="skills_selector"
        )
    
        experience = st.slider("工作经验(年)", 0, 30, 9, key="experience")
        salary = st.slider("期望薪资", 10,3000,50, key="salary")
        
        bio_input = st.text_area(
            "个人简介",
            value=st.session_state.bio,
            placeholder="请简单介绍您的专业背景、职业目标和个人特长和兴趣爱好...",
            key="bio_input"
        )
        st.session_state.bio = bio_input
        cert_input = st.text_area(
        "技能证书",
        value=st.session_state.certificates,
        placeholder="请输入您的技能证书（每行一个证书，例如：Python高级认证/PMP项目管理认证/英语四级/六级）",
        key="cert_input"
        )
        st.session_state.certificates = cert_input  # 双向绑定

        # 联系时间和语言能力
        contact_time = st.time_input("每日最佳联系时间", time(9, 0), key="contact_time")
        # 图片上传区域
    
        uploaded_file = st.file_uploader(
            "上传个人照片",
            type=["jpg", "jpeg", "png"],
            key="photo_upload"
        )
        if uploaded_file is not None:
            st.session_state.uploaded_image = uploaded_file.read()
    with col2:
        st.header("个人简历", divider="blue")
        # 简历顶部布局（头像+基本信息）
        col2_1, col2_2 = st.columns([1, 2])
        
        with col2_1:
            st.subheader(st.session_state.name if 'name' in st.session_state else ' ')
            # 显示上传的图片或占位图
            if st.session_state.uploaded_image:
                st.image(Image.open(io.BytesIO(st.session_state.uploaded_image)), width=150)
            else:
                st.image("https://via.placeholder.com/150", width=150)      
            st.write(f"**职位：** {st.session_state.position if 'position' in st.session_state else "未填写职位"}")
            st.write(f"**电话：** {st.session_state.phone_type if 'phone_type' in st.session_state else ""}")
            st.write(f"**邮箱：** {st.session_state.email if 'email' in st.session_state else ""}")  
            st.write(f"**出生日期:** {st.session_state.birth_date.strftime('%Y/%m/%d') if 'birth_date' in st.session_state else '未填写'}")
        with col2_2:    
            st.write(f"**性别:** {st.session_state.gender if 'gender' in st.session_state else '未填写'}")       
            st.write(f"**学历:** {st.session_state.education if 'education' in st.session_state else '未填写'}")
            st.write(f"**毕业院校:** {st.session_state.school if 'school' in st.session_state else '未填写'}")
            st.write(f"**工作经历:** {st.session_state.experience}年" if 'experience' in st.session_state else "**工作经历:** 未填写")
            st.write(f"**期望薪资:** {st.session_state.salary}元" if 'salary' in st.session_state else "**期望薪资:** 未填写")
            st.write(f"**最佳联系时间:** {st.session_state.contact_time.strftime('%H:%M') if 'contact_time' in st.session_state else '未填写'}")
            st.write(f"**语言能力:** {', '.join(st.session_state.languages) if st.session_state.languages else '未填写'}")   
                
                    
        # 基本信息区块      

        
        # 个人简介区块
        st.markdown("""<hr style='border: 1px solid #1e88e5; margin: 0.5em 0;'>""", unsafe_allow_html=True)
        st.subheader("个人简历")
        if st.session_state.bio:

            st.write(st.session_state.bio)
        else:
            st.write("这个人很神秘，没有留下任何介绍...")    
        st.text(" ")          
        # 专业技能区块
        st.subheader("技能证书")
        if st.session_state.certificates:
            cert_list = [c for c in st.session_state.certificates.split('\n') if c.strip()]
            for cert in cert_list:
                st.markdown(f"📜 {cert}")
        else:       
            st.write("这个人很神秘，没有考到任何证书...")  # 灰色占位提示
        st.markdown("""<hr style='border: 1px solid #1e88e5; margin: 0.5em 0;'>""", unsafe_allow_html=True)
        st.subheader("专业技能")
        if 'skills' in st.session_state and st.session_state.skills:
            cols = st.columns(3)  # 3列布局显示技能
            for i, skill in enumerate(st.session_state.skills):
                cols[i % 3].write(f"• {skill}")
        else:
            st.write("这个人很神秘，不会任何技能...")
with tab2:


    data = pd.DataFrame({
        "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
        "评分": [4.2, 4.5, 4.8, 4.7, 4.3],
        "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
        "人均消费(元)": [15, 20, 25, 35, 55],
        "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
        "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
    })
    restaurant_details = {
        "复记老友粉": {
            "crowd": 80,
            "dishes": ["老友牛肉", "老友猪肉", "炒粉"],
            "image": "https://example.com/laoyoufen.jpg"  # 替换为实际图片URL
        },
        "星艺会尝不忘": {
            "crowd": 60,
            "dishes": ["招牌螺蛳粉", "卤鸭脚", "卤蛋"],
            "image": "https://example.com/xingyihui.jpg"  # 替换为实际图片URL
        },
        "高峰柠檬鸭": {
            "crowd": 70,
            "dishes": ["柠檬鸭", "酸笋炒肉", "白切鸡"],
            "image": "https://example.com/lemonduck.jpg"  # 替换为实际图片URL
        },
        "好友缘": {
            "crowd": 50,
            "dishes": ["海鲜自助", "烤肉", "甜品"],
            "image": "https://example.com/haoyouyuan.jpg"  # 替换为实际图片URL
        },
        "西冷牛排店": {
            "crowd": 65,
            "dishes": ["西冷牛排", "罗宋汤", "沙拉"],
            "image": "https://example.com/xileng.jpg"  # 替换为实际图片URL
        }
    }

    # 添加序号索引
    df = pd.DataFrame(data)
    index = pd.Series([1, 2, 3, 4, 5], name='序号')
    df.index = index

    st.header("🍔 南宁天堂")    
    st.markdown("探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。")

    st.subheader("🍔 南宁天堂")  
    st.map(pd.DataFrame(data))

    st.subheader("⭐ 餐厅评分")  
    st.bar_chart(df, x="餐厅", y="评分")

    st.subheader("💰 不同类型餐厅价格")

    # 餐厅价格数据
    price_data = pd.DataFrame({
        "餐厅类型": ["中餐", "快餐", "自助餐", "西餐"],
        "好友缘": [12, 8.2, 6.0, 5.5],
        "高峰柠檬鸭": [6.8, 9.0, 7.5, 11.2],
        "星艺会尝不忘": [5.5, 7.0, 9.0, 7.0],
        "复记老友粉": [8.0, 9.5, 13.0, 11.8],
        "西冷牛排店": [9.0, 12.5, 5.0, 13.0]
    })

    # 显示价格折线图
    st.line_chart(
        price_data.set_index("餐厅类型"),
        height=400,
        use_container_width=True
    )

    # 用餐高峰数据
    peak_data = pd.DataFrame({
        "时间": ["12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", 
            "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00"],
        "复记老友粉": [40, 70, 80, 65, 50, 40, 35, 30, 25, 20, 30, 45, 60, 55, 50, 40, 30],
        "星艺会尝不忘": [30, 50, 60, 55, 45, 35, 30, 25, 20, 15, 25, 40, 55, 50, 45, 35, 25],
        "高峰柠檬鸭": [25, 35, 45, 55, 45, 40, 40, 45, 40, 35, 45, 65, 85, 80, 70, 55, 45],
        "好友缘": [12, 15, 8.2, 10, 6.0, 8, 5.5, 7, 6, 8, 10, 15, 20, 18, 15, 12, 10],  
        "西冷牛排店": [9.0, 12, 12.5, 10, 5.0, 8, 13.0, 10, 8, 10, 12, 15, 18, 15, 12, 10, 8]
    })

    # 显示高峰时段折线图（使用正确的变量名peak_hours_data）
    st.area_chart(
        peak_data.set_index("时间"),
        height=400,
        use_container_width=True,
    
    )
    st.subheader("📈 年度价格走势（2025）")

    # 定义12个月价格数据（单位：元）
    monthly_price = pd.DataFrame({
        "月份": ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"],
        "复记老友粉": [25, 40, 18, 35, 15, 28, 16, 38, 22, 42, 20, 32],
        "好友缘": [45, 30, 50, 28, 45, 22, 48, 26, 40, 50, 25, 42],
        "星艺会尝不忘": [10, 30, 8, 28, 5, 25, 7, 32, 10, 35, 5, 28],
        "高峰柠檬鸭": [35, 15, 38, 12, 35, 10, 32, 15, 38, 18, 35, 20],
        "西冷牛排店": [70, 40, 75, 35, 68, 38, 72, 40, 75, 45, 70, 50]
    })

    # 绘制折线图（保持颜色一致）
    st.line_chart(
        monthly_price.set_index("月份"),
        height=400,
        use_container_width=True,
        
    )

    # ===== 侧边栏 - 餐厅选择和随机推荐 =====
    st.sidebar.title("🍽️ 南宁天堂")
    selected_restaurant = st.sidebar.selectbox(
        "选择餐厅查看详情",
        data["餐厅"].tolist()
    )

    if st.sidebar.button("🎲 帮我选午餐", type="primary"):
        selected_restaurant = random.choice(data["餐厅"].tolist())
        st.sidebar.success(f"为您推荐: {selected_restaurant}")

    # ===== 主页面布局 =====
    col1, col2 = st.columns([3, 1])

    with col1:
        # 餐厅详情部分
        st.title("🍽️ 餐厅详情")
        st.markdown("选择餐厅查看详情")
        
        # 获取餐厅详情
        restaurant_info = data[data["餐厅"] == selected_restaurant].iloc[0]
        details = restaurant_details.get(selected_restaurant, {})
        
        # 显示餐厅基本信息
        st.header(f"## {selected_restaurant}")
        
        info_col1, info_col2 = st.columns(2)
        with info_col1:
            st.metric("评分", f"{restaurant_info['评分']}/5.0")
        with info_col2:
            st.metric("人均消费", f"{restaurant_info['人均消费(元)']}元")
        
        # 推荐菜品
        st.subheader("推荐菜品")
        if details.get("dishes"):
            for dish in details["dishes"]:
                st.markdown(f"- {dish}")
        
        # 拥挤程度
        st.subheader("当前拥挤程度")
        if "crowd" in details:
            crowd = details["crowd"]
            st.progress(crowd/100, text=f"{crowd}% 拥挤")
        
        # 随机午餐推荐区域
        st.divider()
        st.subheader("今日午餐推荐")
        if st.button("🍚 帮我选午餐", use_container_width=True, type="primary"):
            recommended = random.choice(data["餐厅"].tolist())
            st.success(f"今日推荐: {recommended}({data[data['餐厅'] == recommended].iloc[0]['类型']})")
            if restaurant_details.get(recommended) and restaurant_details[recommended].get("image"):
                st.image(restaurant_details[recommended]["image"], width=300)
            st.write("美味午餐等着你!")
with tab3:


# 定义媒体数据（图片+对应视频）<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=441841347&bvid=BV1hL411S7Qb&cid=1076988324&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
    media_library = {
        "map1": {
            "image_url": "https://media.9game.cn/gamebase/ieu-gdc-pre-process/images/20230328/4/20/2f125d45598aa2cd0947034f9f82381a.png",
            "video_url": "https://cdn.pixabay.com/video/2025/04/29/275633_tiny.mp4"       
        },
        "map2": {
            "image_url": "https://img.pconline.com.cn/images/upload/upc/tx/photoblog/1011/13/c1/5848328_5848328_1289615909062.jpg",
            "video_url": "https://www.w3schools.com/html/movie.mp4",
            
        },
        "map3": {
            "image_url": "https://picx.zhimg.com/v2-531d0ce464a3409581f33c578d225ffd_720w.jpg?source=172ae18b",
            "video_url": "https://media.w3.org/2010/05/sintel/trailer.mp4"
        
        }
    }

    # 初始化session_state
    if 'selected_media' not in st.session_state:
        st.session_state.selected_media = "map1"

    # 页面标题
    st.header("🎬Streamlit视频编辑器")

    # 视频播放区域
    st.subheader("🎬展示集锦")
    current_media = st.session_state.selected_media
    st.video(media_library[current_media]["video_url"])

    # 下拉选择器
    st.subheader("选择媒体")
    selected = st.selectbox(
        "请选择要播放的媒体：",
        options=list(media_library.keys()),
        index=list(media_library.keys()).index(current_media),
        key="media_selector"
    )

    if selected != current_media:
        st.session_state.selected_media = selected
        st.rerun()

    if st.button("map1", key="btn_natural"):
        st.session_state.selected_media = "map1"
        st.rerun()
    st.image(
        media_library["map1"]["image_url"],
        
        use_container_width=True
    )

    if st.button("map2", key="btn_city"):
        st.session_state.selected_media = "map2"
        st.rerun()
    st.image(
        media_library["map2"]["image_url"],
        use_container_width=True
    )
    if st.button("map3", key="map3_city"):
        st.session_state.selected_media = "map3"
        st.rerun()
    st.image(
        media_library["map3"]["image_url"],
        use_container_width=True
    )
with tab4:
    st.title("🕶️ 学生 小吴 - 数字档案")



    # 基础信息章节

    st.header("🔑 基础信息")

    st.text("学生ID: NEO-2023-001")

    st.markdown("**注册时间**: `2023-10-01 08:30:17` | **精神状态**: ✅ 正常")

    st.markdown("**当前教室**: `实训楼301` | **安全等级**: `绝密`")



    # 技能矩阵章节

    st.header("📊 技能矩阵")

    col1, col2, col3 = st.columns(3)

    col1.metric("C语言", "95%", "2%", help="近期训练提升") 

    col2.metric("Python", "87%", "-1%")

    col3.metric("Java", "68%", "-10%", help="用则进废则退")



    # 进度条展示

    st.subheader("Streamlit课程进度")

    st.progress(85, text="Streamlit课程进度")



    # 任务日志章节

    st.header("📝 任务日志")

    mission_data = {

        "日期": ["2023-10-01", "2023-10-05", "2023-10-12"],

        "任务": ["学生数字档案", "课程管理系统", "数据图表展示"],

        "状态": ["✅ 完成", "🕒 进行中", "❌ 未完成"],

        "难度": ["★☆☆☆☆", "★★☆☆☆", "★★★☆☆"]

    }

    mission_df = pd.DataFrame(mission_data)

    st.table(mission_df.style.applymap(

        lambda x: 'color: #0f0' if x == "✅ 完成" else 'color: #ff0')

    )



    # 代码块展示

    st.subheader("🔐 最新代码成果")

    st.code('''def matrix_breach():

        while True:

            if detect_vulnerability():

                exploit()

                return "ACCESS GRANTED"

            else:

                stealth_evade()''', language='python')



    # 动态信息流

    st.write("---")

    st.write("`>> SYSTEM MESSAGE:` 下一个任务目标已解锁...")

    st.write("`>> TARGET:` 课程管理系统")

    st.write("`>> COUNTDOWN:`", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))



    # 终端效果

    st.markdown("""

    系统状态: 在线

    连接状态: 已加密

    """)




            

