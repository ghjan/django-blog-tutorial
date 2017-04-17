**也许是迄今最好最新的 django 中文版入门教程，全部教程请访问：http://zmrenwu.com/category/1/**

**注：教程在陆续发布中，master 分支是已经废弃的代码，请按照教程顺序依次查看各个分支的最新代码**

## 为什么写这个教程？

我从去年开始接触 [Python][1]，为了能让学习 Python 的过程不那么枯燥，我决定一边学习 Python 的同时一边利用所学的东西开发一个网站。在权衡了多个 Python 界流行的 Web 框架后，我决定选择 [django][2]。
[1]: <https://www.python.org/>
[2]: <https://www.djangoproject.com/>

然而 django 在国内的 Web 开发者中使用率其实并不高（不仅仅是 django，包括其他 Python Web 框架例如 [Flask][3] 等也面临同样的境遇），于是寻找合适的学习资料成了一件苦差。在两个多月的时间内，我阅读 [The Django Book2.0 中文版][4]（其内容已经严重过时），然后从网上搜到了一个利用 django 开发一个简单的个人博客的教程，然而其中遇到的各种坑让我在经历了一个月的痛苦发开后彻底放弃了 django。django 高质量的中文学习资料实在太少了，而且中文社区支持也不友好，新人在开发中遇到问题通常求助无门。
[3]: <http://flask.pocoo.org/>
[4]: <http://djangobook.py3k.cn/2.0/>

大概在几个月前，我利用空闲的时间开始学习 django 的官方文档，特别是其[入门教程的 6 个 Parts][5] 循序渐进，既覆盖了 django 大部分的核心特性，又对新人十分友好，这重新激起了我对 django 的兴趣。于是我心血来潮地在网上发起了一个组建 django 五人学习小组的活动，很快便得到了大家的响应。我们以互相分享各自所学的 django 知识并且利用这些知识合作开发一个项目的形式，顺利地开发了一个 [django 个人博客][6]和一个 [django 社区应用][7]，并且还发布了一套 [django 博客教程][8]，但是由于当时自己也是学习 django 不久，对 django 的掌握程度还很不够，教程也比较简略，对想学习 django 的开发者依然不够友好。
[5]: <https://docs.djangoproject.com/en/1.10/intro/>
[6]: <http://zmrenwu.com/>
[7]: <http://www.pythonzh.cn/>
[8]: <http://www.jianshu.com/p/3bf9fb2a7e31>

官方文档的入门教程已经非常好了，但一方面其在语言方面（英语，在一些国内开发者的贡献下现在也有了非官方的中文翻译版本）会对国内的一些开发者产生一定的困扰，另一方面它教我们一步步开发一个简单的投票应用，我感觉这稍稍会有一点枯燥和不实用。所以我决定编写这一套教程，带领想要学习 django 开发的朋友一步步开发一个个人博客，旨在顺便代替 django 官方文档中的入门教程，让开发的过程更加有趣一点，让开发出来的东西更加实用一点。这个博客已经具备个人博客该有的基本功能，我们可以把代码部署到生产服务器上开始使用。

## 谁适合这个教程？

这个教程的目的是一步步地带着大家使用 django 开发一个博客。我假设你以前从未接触过 django 但想成为一名 django 开发者，或者你略微了解过 django 但对如何使用 django 进行开发依然有一些困惑，或者是从其它的 Web 编程框架转过来的开发者。同时我假设你已经具备以下一些基本条件：

- 了解最基本的 Python 语法，或者你从未学习过 Python 但是有学习其他编程语言的经历。
- 了解最基本的 HTML，如果你完全不知道 HTML是个什么东西，建议花费 2-3 天时间学习这个不错的 [HTML 教程][9]。
- （最好具备但不是必须的）HTTP 相关的基本概念，如果你目前完全没有概念也没关系，我会在教程中做适当讲解，但那时如果你依然不懂，建议花费几天时间学习其基本概念。
[9]: <http://www.w3school.com.cn/html/>

总之，[django 博客教程][10]完全面向新人，教程将带你一步步地（Step By Step）使用 django 开发一个博客，教程和官方文档的入门教程一样，涵盖了 django 开发的大部分核心特性，并且尽我所能地做到对新人友好。同时我也为大家提供了一个交流的社区（下面会介绍），以便在开发中遇到问题能得到及时的帮助。
[10]: <https://github.com/zmrenwu/django-blog-tutorial>

## 项目预览与代码托管方式

教程最终开发的博客将是这个样子：[django 博客教程演示项目][6]

代码托管在 [GitHub][10]，每篇教程的代码都放在单独的分支中，分支名看起来像是下面的样子，先后顺序我想应该很容易识别：

Step1_build-development-environment

Step2_create-blog-app

## 互动方式

教程以 Step by Step 的形式，一步步带读者使用 django 开发一个博客。通常情况下，只要你完全依照教程的指导，你将顺利地完成博客系统的开发。但尽管如此，由于开发环境的差异，即使你严格按照教程里的指导，依然有可能遇到无法预料的异常。如果你个人无法解决这些问题，你可以通过以下方式寻求帮助，这可以帮你以最快的速度解决问题。

- 对于简单的问题，请在我[个人博客][6]的评论区留言，每天我都会查看新的留言并且回复相关的问题。

  注：由于本教程会被转载到各大博客平台，不是每个平台下的留言我都会看到并回复。因此建议统一到我个人博客下留言，或者采用下面方式。

- （推荐）对于比较复杂的问题，请到社区发帖求助。同样我也会每天查看新发表的帖子，并且予以回复。在这里求助的另一个好处是其他人也能看到你的问题，并且给予建议和帮助。社区地址：http://pythonzh.cn/

## 版权声明

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/cn/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/3.0/cn/88x31.png" /></a>本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/cn/">知识共享署名-非商业性使用-禁止演绎 3.0 中国大陆许可协议</a>进行许可。

---------from david-----------------
#引入这个项目的目的是为了测试django-redis cache
https://github.com/ghjan/django-blog-tutorial.git


这篇文章里面正好用上了博客的项目
Django1.9开发博客（13）- redis缓存
http://www.cnblogs.com/kuihua/p/5577323.html
blog/cache_manager.py
但是这里其实没有完成，因为还缺乏相应的model定义
所以在blog.models.Post里面添加了一个字段
 click
 还要加上template的修改，博客页面的每次点击都需要统计
    也就是要调用
    update_click
    然后发起一个异步task,这个task里面调用sync_click最终保存到数据库
