from . import main
from flask import render_template, request, redirect, url_for, current_app
import json

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/edit')
def edit():
    return render_template('edit.html')

@main.route('/update', methods=['POST'])
def update():
    # Update the resume data from form submission
    data = current_app.config['data']
    
    # Update basic info
    data['name'] = request.form.get('name', data['name'])
    data['tagline'] = request.form.get('tagline', data['tagline'])
    data['email'] = request.form.get('email', data['email'])
    data['phone'] = request.form.get('phone', data['phone'])
    data['website'] = request.form.get('website', data['website'])
    data['linkedin'] = request.form.get('linkedin', data['linkedin'])
    data['github'] = request.form.get('github', data['github'])
    data['twitter'] = request.form.get('twitter', data['twitter'])
    data['summary'] = request.form.get('summary', data['summary'])
    data['project_intro'] = request.form.get('project_intro', data['project_intro'])
    
    # Update skills
    skills = []
    skill_count = int(request.form.get('skill_count', 0))
    for i in range(skill_count):
        skill_name = request.form.get(f'skill_name_{i}', '')
        skill_level = request.form.get(f'skill_level_{i}', '')
        if skill_name:
            skills.append([skill_name, skill_level])
    data['skills'] = skills
    
    # Update languages
    languages = []
    lang_count = int(request.form.get('lang_count', 0))
    for i in range(lang_count):
        lang_name = request.form.get(f'lang_name_{i}', '')
        lang_level = request.form.get(f'lang_level_{i}', '')
        if lang_name:
            languages.append([lang_name, lang_level])
    data['languages'] = languages
    
    # Update education
    education = []
    edu_count = int(request.form.get('edu_count', 0))
    for i in range(edu_count):
        degree = request.form.get(f'degree_{i}', '')
        school = request.form.get(f'school_{i}', '')
        edu_time = request.form.get(f'edu_time_{i}', '')
        if degree:
            education.append([degree, school, edu_time])
    data['education'] = education
    
    # Update interests
    interests = []
    interest_count = int(request.form.get('interest_count', 0))
    for i in range(interest_count):
        interest = request.form.get(f'interest_{i}', '')
        if interest:
            interests.append(interest)
    data['interests'] = interests
    
    # Update experience
    experience = []
    exp_count = int(request.form.get('exp_count', 0))
    for i in range(exp_count):
        title = request.form.get(f'exp_title_{i}', '')
        date = request.form.get(f'exp_date_{i}', '')
        company = request.form.get(f'exp_company_{i}', '')
        desc = request.form.get(f'exp_desc_{i}', '')
        if title:
            experience.append([title, date, company, desc])
    data['experience'] = experience
    
    # Update projects
    projects = []
    proj_count = int(request.form.get('proj_count', 0))
    for i in range(proj_count):
        proj_name = request.form.get(f'proj_name_{i}', '')
        proj_desc = request.form.get(f'proj_desc_{i}', '')
        proj_link = request.form.get(f'proj_link_{i}', '')
        if proj_name:
            projects.append([proj_name, proj_desc, proj_link])
    data['projects'] = projects
    
    return redirect(url_for('main.index'))
