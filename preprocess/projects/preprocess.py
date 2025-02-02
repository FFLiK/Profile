import copy

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
        if project.get('download') is None:
            description_div.find('a', class_="project-download-link").decompose()
        else :
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
    createHTML(DIRECTORY + "dev-embedded.html", embedded.projects)
    createHTML(DIRECTORY + "dev-game.html", game.projects)
    createHTML(DIRECTORY + "dev-mobile.html", mobile.projects)
    createHTML(DIRECTORY + "dev-web.html", web.projects)
    createHTML(DIRECTORY + "dev-others.html", dev_others.projects)

    createHTML(DIRECTORY + "design-icon.html", icon.projects)
    createHTML(DIRECTORY + "design-layout.html", layout.projects)
    createHTML(DIRECTORY + "design-uiux.html", uiux.projects)
    createHTML(DIRECTORY + "design-video.html", video.projects)
    createHTML(DIRECTORY + "design-others.html", design_others.projects)
    return

if __name__ == '__main__':
    main()