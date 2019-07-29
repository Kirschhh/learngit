import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """base config"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret key'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    FLASKY_MAIL_SENDED = 'jianghan@julanling.com'  # 发件人地址
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'  # 邮件主题前缀


class ProductionConfig(Config):
    """运行环境配置"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(BASEDIR, 'data.sqlite')


config = {
    # 'development': DevelopmentConfig,
    'testing': ProductionConfig,
    # 'production': ProductionConfig,
    # 'default': DevelopmentConfig
}
