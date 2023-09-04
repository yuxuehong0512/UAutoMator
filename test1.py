# author_='Yuxuehong';
# date: 2023/9/1 15:53

import uiautomator2 as u2

d = u2.connect()  #第一步：初始化

#直接复制过来的都是元素的定位方式，不带元素的操作
d(text="读书屋").click()
d(text="书城").click()
d(resourceId="com.zhao.myreader:id/iv_search").click()
d(resourceId="com.zhao.myreader:id/et_search_key").click()
d.send_keys("大佬她不可能当女配", clear=True)
d(resourceId="com.zhao.myreader:id/tv_search_conform").click()
d.xpath('//*[@resource-id="com.zhao.myreader:id/ll_title_back"]/android.widget.ImageView[1]').click()