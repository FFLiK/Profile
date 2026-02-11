import copy
import json

from bs4 import BeautifulSoup

from projects.dev import desktop
from projects.dev import embedded
from projects.dev import game
from projects.dev import mobile
from projects.dev import web
from projects.dev import others as dev_others

from projects.design import icon
from projects.design import layout
from projects.design import uiux
from projects.design import video
from projects.design import others as design_others

def writeProjects(content, projects):
    cnt = 0
    template = content.find('div', class_='project-box')

    for project in projects:
        if project.get('hidden') is not None :
            continue

        project_div = copy.deepcopy(template)
        description_div = project_div.find('div', class_='project-description-box')
        description_div.find('h4', class_="project-title").string = project['title']
        description_div.find('small', class_="project-date").string = project['date']
        description_div.find('p', class_="project-summary").string = project['summary']
        description_div.find('div', class_="project-description")['class'] = copy.deepcopy(description_div.find('div', class_="project-description")['class'])
        description_div.find('div', class_="project-description")['class'].append("openclose-linker" + str(cnt))
        description_div.find('small', class_="project-description-text").append(BeautifulSoup(project['description'], 'html.parser'))
        description_div.find('a', class_="openclose")['href'] = "openclose-linker" + str(cnt)
        for tag in project['tag']:
            a = copy.deepcopy(description_div.find('a', class_="project-tag"))
            a.string = tag
            description_div.find('div', class_="project-tag-box").append(a)
        description_div.find('a', class_="project-tag").decompose()

        if project.get('open') is None:
            description_div.find('a', class_="project-open-link").decompose()
        else :
            description_div.find('a', class_="project-open-link")['href'] = project['open']
            if "display" in project['open']:
                description_div.find('a', class_="project-open-link")['onclick'] = "window.open(this.href,'Display','width=800, height=800'); return false;"
        if project.get('download') is None:
            description_div.find('a', class_="project-download-link").decompose()
        else :
            if project['download'] == "file":
                file_name = project['open'].split('=')[-1]
                #read json
                with open('../../display/projects.json', 'r', encoding="utf-8") as file:
                    projects = file.read() #json file
                    projects = json.loads(projects)
                description_div.find('a', class_="project-download-link")['href'] = "https://assets.profile.fflik.kr/" + projects[file_name]['res'];
                description_div.find('a', class_="project-download-link")['download'] = projects[file_name]['title']
            else:
                description_div.find('a', class_="project-download-link")['href'] = project['download']
        if project.get('github') is None:
            description_div.find('a', class_="project-github-link").decompose()
        else :
            description_div.find('a', class_="project-github-link")['href'] = project['github']

        icon_div = project_div.find('div', class_='project-icon-box')
        if project['icon'] == "":
            icon_div.decompose()
        else:
            icon_div.find('img')['src'] = project['icon']
            icon_div.find('img')['alt'] = project['title']

        content.find('div', class_='project-division').append(project_div)

        cnt += 1

    template.decompose()

    return

def createHTML(filename, project) :
    TEMPLATE_FILE = 'template.html'

    with open(TEMPLATE_FILE, 'r', encoding="utf-8") as file:
        template = file.read()

    html = BeautifulSoup(template, 'html.parser')
    writeProjects(html, project)

    with open(filename, 'w', encoding="utf-8") as file:
        file.write(str(html))
    return


def main() :
    DIRECTORY = '../../pages/projects/'

    createHTML(DIRECTORY + "dev-desktop.html", desktop.projects)
    print("Create dev-desktop.html")
    createHTML(DIRECTORY + "dev-embedded.html", embedded.projects)
    print("Create dev-embedded.html")
    createHTML(DIRECTORY + "dev-game.html", game.projects)
    print("Create dev-game.html")
    createHTML(DIRECTORY + "dev-mobile.html", mobile.projects)
    print("Create dev-mobile.html")
    createHTML(DIRECTORY + "dev-web.html", web.projects)
    print("Create dev-web.html")
    createHTML(DIRECTORY + "dev-others.html", dev_others.projects)
    print("Create dev-others.html")
    createHTML(DIRECTORY + "design-icon.html", icon.projects)
    print("Create design-icon.html")
    createHTML(DIRECTORY + "design-layout.html", layout.projects)
    print("Create design-layout.html")
    createHTML(DIRECTORY + "design-uiux.html", uiux.projects)
    print("Create design-uiux.html")
    createHTML(DIRECTORY + "design-video.html", video.projects)
    print("Create design-video.html")
    createHTML(DIRECTORY + "design-others.html", design_others.projects)
    print("Create design-others.html")
    return

if __name__ == '__main__':
    main()