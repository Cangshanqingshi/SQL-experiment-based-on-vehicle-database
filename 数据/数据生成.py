import xlrd
import xlwt
import faker
import random

if __name__ == '__main__':
    workbook = xlwt.Workbook()
    datestyle = xlwt.XFStyle()
    datestyle.num_format_str = 'yyyy-mm-dd'
    fk = faker.Faker(locale='zh_CN')

    # 生成客户信息
    costumer_num = 15
    worksheet = workbook.add_sheet('客户')
    worksheet.write(0, 0, '客户编号')
    worksheet.write(0, 1, '姓名')
    worksheet.write(0, 2, '地址')
    worksheet.write(0, 3, '电话')
    worksheet.write(0, 4, '性别')
    worksheet.write(0, 5, '年收入')
    worksheet.write(0, 6, '生日')

    uids = []
    for i in range(costumer_num):
        uid = fk.numerify()
        while uid in uids:
            uid = fk.numerify()
        uids.append(uid)

    for i in range(costumer_num):
        worksheet.write(i + 1, 0, uids[i])
        if random.random() > 0.5:
            worksheet.write(i + 1, 4, '男')
            worksheet.write(i + 1, 1, fk.name_male())
        else:
            worksheet.write(i + 1, 4, '女')
            worksheet.write(i + 1, 1, fk.name_female())
        worksheet.write(i + 1, 2, fk.address())
        worksheet.write(i + 1, 3, fk.phone_number())
        worksheet.write(i + 1, 5, random.randrange(12000, 600000, 4945))
        worksheet.write(i + 1, 6, fk.date_of_birth(), datestyle)

    # 生成经销商信息
    distributor_num = 8
    worksheet = workbook.add_sheet('经销商')
    worksheet.write(0, 0, '公司名')
    worksheet.write(0, 1, '地址')
    worksheet.write(0, 2, '级别')

    distributor_names = []
    for i in range(distributor_num):
        distributor_name = fk.unique.company()
        for ch in ['网络', '科技', '传媒', '信息']:
            distributor_name = distributor_name.replace(ch, '销售')
        for ch in ['电脑', '计算机']:
            distributor_name = distributor_name.replace(ch, '汽车')
        while distributor_name in distributor_names:
            distributor_name = fk.unique.company()
            for ch in ['网络', '科技', '传媒', '信息']:
                distributor_name = distributor_name.replace(ch, '销售')
            for ch in ['电脑', '计算机']:
                distributor_name = distributor_name.replace(ch, '汽车')
        worksheet.write(i + 1, 0, distributor_name)
        worksheet.write(i + 1, 1, fk.address())
        worksheet.write(i + 1, 2, random.randint(1, 3))

    # 保存
    workbook.save('./数据.xls')
