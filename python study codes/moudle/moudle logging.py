## Python的日志记录工具----logging模块


## logging 中的几个概念：

    # Logger：日志记录器，是应用程序中可以直接使用的接口。
    # Handler：日志处理器，用以表明将日志保存到什么地方以及保存多久。
    # Formatter：格式化，用以配置日志的输出格式。

#上述三者的关系是：一个 Logger 使用一个 Handler，一个 Handler 使用一个 Formatter。



##使用logging模块
#logging(日志)模块用于跟踪程序的运行状态，它把程序的运行状态划分为不同的级别

    # DEBUG:调试状态
    # INFO: 正常运行状态
    # WORNING: 警告状态
    # ERROR: 错误状态
    # CRITICAL: 严重错误状态

##logging 模块提供了一组日志函数：debug()、info()、warining()、error()和critical()


#演示将日志信息打印在控制台
import logging
logging.debug('debug信息')
logging.warning('只有这个会输出......')     # 默认的等级是WARNING, 输出：WARNING:root:只有这个会输出......
logging.info('info信息')

##使用logging.basicConfig()方法设置日志信息的格式和日志函数的响应级别

# import logging          #导入日志模块
# logging.basicConfig(
#     format = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s:%(message)s', 
#     level=logging.DEBUG)

# logging.debug('debug信息')
# logging.info('info信息')
# logging.warning('warning信息')
# logging.error('error信息')
# logging.critical('critial信息')


# print('\n----------------------------------14----------------------------------------\n')

# ##演示使用logging模块把日志信息输出到外部文件

# import logging
# #配置日志文件和日志信息的格式
# logging.basicConfig( filename='test.log',
#                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]',
#                      level=logging.DEBUG,
#                       filemode='a',
#                        datefmt='%Y-%m-%d%I:%M:%S %p' )
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)   #保存n的值到日志文件中
# print(10 / n)

