# -*- coding: UTF-8 -*-
import os
import smtplib
from email.header import make_header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:
    def __init__(self,
                 port=465,  # 邮件端口
                 mail_host="smtp.qq.com",  # 邮件服务器地址  eg:smtp.163.com、210.77.136.200...
                 mail_user="1538804595@qq.com",  # 邮箱登录用户名
                 mail_pass="zkgqfosjdswihacc",  # 邮箱登录密码（打开imap的使用验证码，gmail使用密码）
                 mail_sender="1538804595@qq.com",  # 邮件发送人
                 ):
        # 第三方 SMTP 服务
        self.port = port
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.mail_sender = mail_sender

    def SendHtmlMail(self, mail_to_list, mail_subject, mail_body, file_list, mail_cc_list, mail_bcc_list):
        """
        发送Html邮件
        :param mail_to_list: 接收者邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']
        :param mail_subject: 邮件主题
        :param mail_body: 邮件体主题内容
        :param file_list: 附件列表，就文件名列表（包含路径）
        :param mail_cc_list: 抄送邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']，默认不传
        :param mail_bcc_list: 密送邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']，默认不传
        :return:
        """
        message = MIMEText(mail_body, _subtype='html', _charset='gb2312')
        message['Subject'] = mail_subject
        message['From'] = self.mail_sender
        if len(mail_cc_list) > 0:
            message['Cc'] = ",".join(mail_cc_list)
            mail_to_list.extend(mail_cc_list)
        if len(mail_bcc_list) > 0:
            message['Bcc'] = ",".join(mail_bcc_list)
            mail_to_list.extend(mail_bcc_list)

        try:
            smtpObj = smtplib.SMTP(self.mail_host, self.port)
            # smtpObj.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
            # smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.mail_sender, mail_to_list, message.as_string())
            smtpObj.close()
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件")

    def SendMailAttach(self, mail_to_list, mail_subject, mail_body, file_list, mail_cc_list):
        '''
        发送带附件的邮件
        :param mail_to_list: 接收者邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']
        :param mail_subject: 邮件主题
        :param mail_body: 邮件体主题内容
        :param file_list: 附件列表，就文件名列表（包含路径）
        :param mail_cc_list: 抄送邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']，默认不传
        :param mail_bcclist: 密送邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']，默认不传
        :return:
        '''
        msg = MIMEMultipart()
        message = MIMEText(mail_body, _subtype='plain', _charset='utf-8')
        msg.attach(message)

        # 构造附件
        for f in file_list:
            if os.path.isfile(f):
                att = MIMEText(open(f, 'rb').read(), 'base64', 'utf-8')
                att["Content-Type"] = 'application/octet-stream'
                att["Content-Disposition"] = "attachment;filename='%s'" % make_header([(os.path.basename(f), 'UTF-8')]).encode('UTF-8')
                msg.attach(att)

        msg['Subject'] = mail_subject
        msg['From'] = self.mail_sender
        msg['To'] = ",".join(mail_to_list)
        if len(mail_cc_list) > 0:
            msg['Cc'] = ",".join(mail_cc_list)
            mail_to_list.extend(mail_cc_list)
        # if len(mail_bcclist) > 0:
        #     msg['Bcc'] = ",".join(mail_bcclist)
        #     mail_tolist.extend(mail_bcclist)

        message = ''
        try:
            server = smtplib.SMTP()
            server.connect(self.mail_host)
            server.login(self.mail_user, self.mail_pass)
            server.sendmail(self.mail_sender, mail_to_list, msg.as_string())
            server.close()
            result = '邮件发送成功'

        except smtplib.SMTPException as e:
            # print "Error: 无法发送邮件", e
            message = 'Error: 无法发送邮件:'
        return message

    def SendMail(self, mail_subject, mail_body, mail_to_list, mail_cc_list):
        '''
        发送普通邮件
        :param mail_to_list: 接收者邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']
        :param mail_subject: 邮件主题
        :param mail_body: 邮件体主题内容
        :param fileList: 附件列表，就文件名列表（包含路径）
        :param mail_cc_list: 抄送邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']，默认不传
        :param mail_bcclist: 密送邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']，默认不传
        :return:
        '''
        message = MIMEText(mail_body, _subtype='plain', _charset='utf-8')
        message['Subject'] = mail_subject
        message['From'] = self.mail_sender
        if mail_to_list:
            message['To'] = ",".join(mail_to_list)
        if len(mail_cc_list) > 0:
            message['Cc'] = ",".join(mail_cc_list)
            mail_to_list.extend(mail_cc_list)

        result = ''
        try:
            server = smtplib.SMTP()
            server.connect(self.mail_host)
            server.login(self.mail_user, self.mail_pass)
            server.sendmail(self.mail_sender, mail_to_list, message.as_string())
            server.close()
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件")


mail = Mail()
# mail.SendMail("test", "测试展鸿第三封邮件", ['fenyong258@163.com', 'xiaoMa@qq.com'], [])
mail.SendMailAttach(['fenyong258@163.com', 'xiaoMa@qq.com'], "test", "测试展鸿第三封邮件",
                    [r"C:\Users\Administrator\Desktop\2022年储蓄余额通报（11月）—原.xlsx"], [])
