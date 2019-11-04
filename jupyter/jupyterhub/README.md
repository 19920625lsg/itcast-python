# JupyterHub学习笔记

>+ 官网： https://github.com/jupyterhub/jupyterhub
>+ 详细教程：https://jupyterhub.readthedocs.io/en/stable/
>+ 从零开始安装JupyterHub教程：https://zero-to-jupyterhub.readthedocs.io/en/latest/
>+ REST接口的详细说明：http://petstore.swagger.io/?url=https://raw.githubusercontent.com/jupyterhub/jupyterhub/master/docs/rest-api.yml#/
>+ Hub的详细配置参考：https://zero-to-jupyterhub.readthedocs.io/en/latest/reference.html#id1
>+ Hub认证文档：http://jupyterhub.readthedocs.io/en/latest/api/auth.html
>+ jupyterhub_config.py设置 https://jupyterhub.readthedocs.io/en/stable/getting-started/config-basics.htmlhttps://jupyterhub.readthedocs.io/en/stable/getting-started/config-basics.html
>+ Hub的OAuth认证：https://github.com/jupyterhub/oauthenticator


## 安装方式

### 本地安装
```bash
npm install -g configurable-http-proxy
python3 -m pip install jupyterhub 
```

### Docker 安装

```bash
docker pull jupyterhub/jupyterhub
```

### 启动

```bash
docker run -p 8000:8000 -d --name jupyterhub jupyterhub/jupyterhub jupyterhub
```

## 有用的命令

+ 产生配置文件：`jupyterhub --generate-config`
+ 以指定文件启动jupyterhub:`jupyterhub -f /path/to/jupyterhub_config.py`
+ 详细的配置教程见：[配置教程](https://jupyterhub.readthedocs.io/en/stable/getting-started/config-basics.html)


