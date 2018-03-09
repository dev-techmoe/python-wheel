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
* `config.py` - yaml格式设定载入模块
    支持导入yaml格式配置文件。   
    主要方法：
    * `load(text)` 载入yaml字符串
    * `load_file(file_path)` 读取yaml格式配置文件
    * `get(key)` 读取设置，支持以`.`作为分隔读取多层配置
        例子：
        ```
        {
            'a': {
                'b': {
                    'c': 'd'
                }
            }
        }
        ```
        这样的格式便可以用`get('a.b.c')`去读取。   
        提供默认值功能，使用前请自行填充代码内`default_config`这个dict
* `title.py` - 更改脚本运行窗口标题，多平台支持适配中  
    此模块已经在Windows(PowerShell、cmd)、Linux(Ubuntu Gnome Terminal)中测试正常运行。  
    OSX暂时还没测试，希望有人能够帮忙测试OSX下是否能够正常工作，请将结果提交至issue，谢谢  
    使用方法：
    ```python
    import title
    title.update('Hello World')
    ```
    脚本自带一个demo，可以通过直接运行此模块（`python -m`）来观察效果。  
    Linux下使用这个脚本需要注意一个问题，为了保证结果正常每次更新标题的时候都会flush掉stdout的buffer，请注意确认这一点不会对你的程序造成问题。


## link
* 我的主页 - [lolicookie](https://lolicookie.com)
* 我的博客 - [lighthouse](https://lighthouse.lolicookie.com)

## license
MIT
