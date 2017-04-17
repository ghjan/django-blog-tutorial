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
