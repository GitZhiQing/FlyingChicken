from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user

from app import app, db
from app.models import Admins, Records, Event


@app.route("/")
def index():
    """首页，签到页面"""
    return render_template("index.html", event=Event.query.first())


@app.route("/login", methods=["GET", "POST"])
def login():
    """登录"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            flash("用户名或密码不能为空")
            return redirect(url_for("login"))

        user = Admins.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            login_user(user)
            flash("登录成功")
            return redirect(url_for("admin"))
        flash("用户名或密码错误")
        return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    """注销"""
    logout_user()
    flash("您已退出登录")
    return redirect(url_for("index"))


@app.route("/admin")
@login_required
def admin():
    """后台查看签到记录，需要登录"""
    return render_template(
        "admin.html",
        records=Records.query.all(),
        username=current_user.username,
        event=Event.query.first(),
    )


@app.route("/delete/<int:record_id>")
@login_required
def delete_record(record_id):
    """删除签到记录"""
    record = Records.query.get_or_404(record_id)
    db.session.delete(record)
    db.session.commit()
    flash("记录删除成功")
    return redirect(url_for("admin"))


@app.route("/set_event", methods=["POST"])
@login_required
def set_event():
    """设置活动"""
    name = request.form.get("name").strip()
    date = request.form.get("date")
    desc = request.form.get("desc").strip()
    location = request.form.get("location").strip()
    if not name or not date or not desc or not location:
        flash("所有字段都是必填的")
        return redirect(url_for("admin"))

    Event.set_event(name, date, desc, location)
    flash("活动设置成功")
    return redirect(url_for("admin"))


@app.route("/sign_in", methods=["POST"])
def sign_in():
    """签到"""
    name = request.form.get("name")
    phone = request.form.get("phone")
    if not name or not phone:
        return "姓名或手机号不能为空"
    record = Records(name=name, phone=phone)
    db.session.add(record)
    db.session.commit()
    flash("签到成功")
    return redirect(url_for("index"))
