#coding:utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.163.com')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '@163.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '')
    UP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static\\uploads")
    PAGE_SET = 10
    #MAIL_PORT = 25
    #MAIL_USE_TLS = True
    #FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    #FLASKY_MAIL_SENDER = 'Flasky Admin <1348313766@qq.com>'
    #FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30
    FLASKY_SLOW_DB_QUERY_TIME=0.5

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'bbs_test'
    USERNAME = 'root'
    PASSWORD = 'root'
    # dialect+driver://username:password@host:port/database
    SQLALCHEMY_DATABASE_URI= "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(username=USERNAME,
                                                                                               password=PASSWORD,
                                                                                               host=HOSTNAME, port=PORT,
                                                                                               db=DATABASE)




# class TestingConfig(Config):
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
#         'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
#     WTF_CSRF_ENABLED = False
#
#
# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#         'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#
#     @classmethod
#     def init_app(cls, app):
#         Config.init_app(app)
#
#         # email errors to the administrators
#         import logging
#         from logging.handlers import SMTPHandler
#         credentials = None
#         secure = None
#         if getattr(cls, 'MAIL_USERNAME', None) is not None:
#             credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
#             if getattr(cls, 'MAIL_USE_TLS', None):
#                 secure = ()
#         mail_handler = SMTPHandler(
#             mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
#             fromaddr=cls.FLASKY_MAIL_SENDER,
#             toaddrs=[cls.FLASKY_ADMIN],
#             subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' Application Error',
#             credentials=credentials,
#             secure=secure)
#         mail_handler.setLevel(logging.ERROR)
#         app.logger.addHandler(mail_handler)
#
#
# class HerokuConfig(ProductionConfig):
#     SSL_DISABLE = bool(os.environ.get('SSL_DISABLE'))
#
#     @classmethod
#     def init_app(cls, app):
#         ProductionConfig.init_app(app)
#
#         # handle proxy server headers
#         from werkzeug.contrib.fixers import ProxyFix
#         app.wsgi_app = ProxyFix(app.wsgi_app)
#
#         # log to stderr
#         import logging
#         from logging import StreamHandler
#         file_handler = StreamHandler()
#         file_handler.setLevel(logging.WARNING)
#         app.logger.addHandler(file_handler)
#
#
# class UnixConfig(ProductionConfig):
#     @classmethod
#     def init_app(cls, app):
#         ProductionConfig.init_app(app)
#
#         # log to syslog
#         import logging
#         from logging.handlers import SysLogHandler
#         syslog_handler = SysLogHandler()
#         syslog_handler.setLevel(logging.WARNING)
#         app.logger.addHandler(syslog_handler)


config = {
    'development': DevelopmentConfig,
    # 'testing': TestingConfig,
    # 'production': ProductionConfig,
    # 'heroku': HerokuConfig,
    # 'unix': UnixConfig,

    'default': DevelopmentConfig
}