# python-wheel
个人自用轮子集

## 各轮子的介绍
* `base_logger.py` 控制台输出着色的logger生成器  
    ![image](https://user-images.githubusercontent.com/7919562/36772068-c05421f8-1c8e-11e8-85bd-de670d88133f.png)
    使用方法：  
    ```python
    import base_logger

    logger = base_logger.getLogger(__name__)
    ```  
    使用了模块[colorlog](https://github.com/borntyping/python-colorlog)自带的formatter作为着色实现。  
    必须指定logger名（唯一参数）否则只能会获取到rootlogger，并且会重复配置handler导致输出消息重复  
    目前仅仅写了StreamHandler，也就是console output  
    

## license
MIT