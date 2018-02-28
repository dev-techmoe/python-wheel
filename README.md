# python-wheel
个人自用轮子集

## 说明
这个repo整理了我python开发过程中的一些用到的、我觉得可以拿来复用的代码合集。  
搜集自他人的代码我都会显著标明源地址，如果有疏漏还请及时提交issue告知我。  
欢迎star

## 各轮子的介绍
* `base_logger.py` - 控制台输出着色的logger生成器  
    ![image](https://user-images.githubusercontent.com/7919562/36772068-c05421f8-1c8e-11e8-85bd-de670d88133f.png)
    使用方法：  
    ```python
    import base_logger

    logger = base_logger.getLogger(__name__)
    ```  
    使用了模块[colorlog](https://github.com/borntyping/python-colorlog)自带的formatter作为着色实现。  
    必须指定logger名（唯一参数）否则只能会获取到rootlogger，并且会重复配置handler导致输出消息重复  
    目前仅仅写了StreamHandler，也就是console output  
* `decode_js_packed_codes.py` - 反解Js Packer生成的加密代码  
    此代码来自于[youtube-dl](https://github.com/rg3/youtube-dl/blob/befa4708fd2165b85d04002c3845adf191d34302/youtube_dl/utils.py#L3633)  
    当初写dmzj漫画批量下载器时用的一个工具，可以反解jspacker生成的加密代码  
    JS Packer加密后的代码的一个特征就是是以`eval(function(p,a,c,k,e,d)`这样开头的代码，凡是遇到这样的代码基本可以尝试用这个轮子去解  
    输入时记住参数值要包括`eval()`结构  
    相关资料：[Python: packer方式加密js代码之解密函数](http://www.cnblogs.com/crwy/p/7659579.html)

## link
* 我的主页 - [lolicookie](https://lolicookie.com)
* 我的博客 - [lighthouse](https://lighthouse.lolicookie.com)

## license
MIT