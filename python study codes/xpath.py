## XPath 和 lxml

# http://www.ityouknow.com/python/2019/11/20/python-xpath-064.html


# XPath 全称为 Xml Path Language，即 Xml 路径语言，是一种在 Xml 文档中查找信息的语言。
# 它提供了非常简洁的路径选择表达式，几乎所有的节点定位都可以用它来选择。
# XPath 可以用于 Xml 和 Html，在爬虫中经常使用 XPath 获取 Html 文档内容。


## lxml 是 Python 语言用 Xpath 解析 XML、Html文档功能最丰富的、最容易的功能模块



#在 XPath 中有七种节点分别是元素、属性、文本、文档、命名空间、处理指令、注释，前3种节点为常用节点

""" 

<!DOCTYPE html>
<html>
    <body>
        <div>
            <!-- 这里是注释 -->
            <h4>手机品牌商<span style="margin-left:10px">4</span></h4>
            <ul>
               <li>小米</li>
               <li>华为</li> 
               <li class='blank'> OPPO </li>
               <li>苹果</li>
            </ul>
        </div>
        <div>
            <h4>电脑品牌商<span style="margin-left:10px">3</span></h4>
            <ul class="ul" style="color:red">
                <li>戴尔</li> 
                <li>机械革命</li> 
                <li>ThinkPad</li>
            </ul>
        </div>
    </body>
</html> 

"""