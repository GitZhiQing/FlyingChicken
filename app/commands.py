import click
from app import app, db
from app.models import Admins


@app.cli.command()
@click.option("--drop", is_flag=True, help="删除后再创建")
@click.option("--admin", is_flag=True, help="初始化创建管理员账户")
def initdb(drop, admin):
    """初始化数据库
    flask initdb # 初始化数据库
    flask initdb --drop # 删除后再初始化数据库
    flask initdb --admin # 初始化创建管理员账户
    """
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("初始化数据库完成.")

    if admin:
        username = click.prompt("请输入管理员用户名")
        password = click.prompt(
            "请输入管理员密码", hide_input=True, confirmation_prompt=True
        )
        admin_user = Admins(username=username)
        admin_user.set_password_hash(password)
        db.session.add(admin_user)
        db.session.commit()
        click.echo("管理员账户创建完成.")
