# python-wheel
个人自用轮子集

## 各轮子的介绍
* `base_logger.py` logger生成器  
    使用方法：  
    ```python
    import base_logger

    logger = base_logger.getLogger(__name__)
    ```
    必须指定logger名（唯一参数）否则只能会获取到rootlogger，并且会重复配置handler导致输出消息重复
    目前仅仅写了StreamHandler，也就是console output

## license
MIT