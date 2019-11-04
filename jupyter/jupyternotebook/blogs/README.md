# 从博客及网上文章学习JupyterHub的搭建以及自定义

## [Docker： 使用jupyter notebook基础镜像搭建自己的 pytorch 开发环境](https://blog.csdn.net/jianchengss/article/details/78224778)

# jupter notebook远程访问的的命令

> `docker run -d -p 8888:8888 jupyter/datascience-notebook:281505737f8a start-notebook.sh --NotebookApp.password='sha1:8c91d5ae94a9:8bf5bbb5ee10c497f4f64a24ae57e18aca26bc2f'`

上面的password是通过

```python
import IPython
IPython.lib.passwd()
```

> 更详细的参数见：[docker-stacks教程](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html#notebook-options)

来生成的

> 最好尝试通过支持更多语言来自定义镜像。写一个自己的Dockerfile吧，build一个新的镜像，push到dockerhub上去。然后再就可以给公司用了。
然后自己再实现一套安全认证和访问功能，默认密码用W3加密后的

# 保存Docker镜像以及导入镜像
[Docker镜像保存为文件及从文件导入镜像](https://blog.csdn.net/anxpp/article/details/51810776)

# 给容器重命名
` docker container rename e95f5fa8349b l00379880_datascience_notebook`
