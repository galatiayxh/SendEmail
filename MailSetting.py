# -*- coding: utf-8 -*-
# 配置文件类

class MailSetting:
    def __init__(self):
        # 由于机器端口控制，目前只能用公司邮箱
        # 邮件端口
        # self.port = 465
        self.port = 465

        # 邮件服务器地址
        self.mail_host = '210.77.136.200'

        # 接收人邮件地址（需要修改）改成你自己的，发送人和接收人可以用一个地址
        self.mail_receive_user = '360648011@qq.com'

        # self.mail_receive_user = 'shaodd@sina.com'

        # 发送人邮件地址（需要修改）改成你自己的，
        self.mail_send_user = 'user@ctrchina.cn'

        # 邮件登录用户名 （需要修改）
        self.mail_user = 'user'

        # 登录用密码（需要修改）
        self.mail_pass = "password"

        def __init__(self,
                     port=465,  # 邮件端口
                     mail_host="smtp.qq.com",  # 邮件服务器地址  eg:smtp.163.com、210.77.136.200...
                     mail_user="galatia",
                     mail_sender="galatia2077@qq.com",  # 邮件发送人
                     mail_pass="zkgqfosjdswihacc",  # 口令
                     mail_receiver="fenyong258@163.com"  # 邮件接收人
                     ):
            # 第三方 SMTP 服务
            self.port = port
            self.mail_host = mail_host
            self.mail_user = mail_user
            self.mail_pass = mail_pass
            self.mail_sender = mail_sender
            self.mail_receiver = mail_receiver