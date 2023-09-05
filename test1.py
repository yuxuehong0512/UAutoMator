# author_='Yuxuehong';
# date: 2023/9/1 15:53

import uiautomator2 as u2

d = u2.connect()  #第一步：初始化

#直接复制过来的都是元素的定位方式，不带元素的操作

#启动应用
d.app_start("com.zhao.myreader") #使用包名启动应用
#d(text="读书屋").click()

ele1 = d(text="书城")

ele2 = d.xpath('//*[@text="书城"]')

print(ele1) # <uiautomator2._selector.UiObject object at 0x00000248E1DA1430> 返回的是一个元素的实例对象

print(ele2) # XPathSelector(//*[@text="书城"] 返回的是一个元素对象

#ele1是可以send_keys的，ele2是没有send_keys的使用set_text

ele1.screenshot()
ele2.screenshot()

# d(resourceId="com.zhao.myreader:id/et_search_key").click()
# d.send_keys("大佬她不可能当女配", clear=True)
# d(resourceId="com.zhao.myreader:id/tv_search_conform").click()
# d.xpath('//*[@resource-id="com.zhao.myreader:id/ll_title_back"]/android.widget.ImageView[1]').click()
d.app_stop("com.zhao.myreader") # 使用包名停止应用