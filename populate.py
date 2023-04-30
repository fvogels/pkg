from __future__ import annotations
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime


uri = "localhost:27017"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.pkg
graph = db.graph



class NodeId:
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    def link(self, *nodes: NodeId):
        for node in nodes:
            link(node.id, self.id)
        return self



def find_node_with_name(name):
    return graph.find_one({'name': name})


def add_node(*, name, **fields) -> NodeId:
    if node := graph.find_one({'name': name}):
        return NodeId(node['_id'])
    else:
        fields = {
            'date': datetime.utcnow(),
            'name': name,
            'links': [],
            **fields
        }
        return NodeId(graph.insert_one(fields).inserted_id)


def add_url(*, name, url, **kwargs):
    return add_node(
        name=name,
        url=url,
        protocol='url',
        **kwargs,
    )


def add_pdf(*, name, authors, filename, **kwargs):
    return add_node(
        name=name,
        authors=authors,
        protocol='pdf',
        filename=filename,
        **kwargs,
    )


def link(from_node, to_node):
    filter = {'_id': from_node}
    update = { '$addToSet': { 'links': to_node } }
    graph.update_one(filter, update)


math = add_node(name='Mathematics')
software_development = add_node(name='Software Development')
programming_language = add_node(name='Programming Language').link(software_development)
proof_assistant = add_node(name='Proof Assistant').link(math)
functional_programming = add_node(name='Functional Programming').link(programming_language)
object_oriented_programming = add_node(name='Object Oriented Programming').link(programming_language)
concurrent_programming = add_node(name='Concurrent Programming').link(programming_language)
logic_programming = add_node(name='Logic Programming').link(programming_language)
type_system = add_node(name='Type System').link(programming_language)
dynamically_typed = add_node(name='Dynamic Typing').link(type_system)
statically_typed = add_node(name='Static Typing').link(type_system)
dependent_typing = add_node(name='Dependent Typing').link(type_system)
computer_science = add_node(name='Computer Science')
webdev = add_node(name='Web Development').link(software_development)
frontend = add_node(name='Front End').link(webdev)
backend = add_node(name='Back End').link(webdev)
latex = add_node(name='LaTeX')
git = add_node(name='Git')
linux = add_node(name='Linux')
unix = add_node(name='Unix')
flask = add_node(name='Flask')
ai = add_node(name='Artificial Intelligence')
machine_learning = add_node(name='Machine Learning')
computer_architecture = add_node(name='Computer Architecture')
security = add_node(name='Security')
database = add_node(name='Database')
data = add_node(name='Data')
graphics = add_node(name='Graphics')
raytracing = add_node(name='Ray Tracing').link(graphics)
parallelism = add_node(name='Parallelism').link(graphics)
economics = add_node(name='Economics')
politics = add_node(name='Politics')
shell_scripting = add_node(name='Shell Scripting')
rest = add_node(name='REST')
unit_testing = add_node(name='Unit Testing')
tdd = add_node(name='Test Driven Development')
bdd = add_node(name='Behavior Driven Development')
azure = add_node(name='Azure')
devops = add_node(name='DevOps')
microservice = add_node(name='Microservice')

library = add_node(name='Library')
book = add_node(name='Book')
free = add_node(name='Free')
reference = add_node(name='Reference')
monad = add_node(name='Monad')
video = add_node(name='Video')
tutorial = add_node(name='Tutorial')
movie = add_node(name='Movie')

haskell = add_url(
    name='Haskell',
    url='https://www.haskell.org/'
).link(programming_language, statically_typed, functional_programming)
typescript = add_url(
    name='TypeScript',
    url='https://www.typescriptlang.org/'
).link(programming_language, statically_typed, object_oriented_programming, functional_programming)
javascript = add_node(name='JavaScript').link(programming_language, dynamically_typed, functional_programming, object_oriented_programming)
csharp = add_node(name='C#').link(programming_language, statically_typed, object_oriented_programming)
c = add_node(name='C').link(programming_language, statically_typed)
cpp = add_node(name='C++').link(programming_language, statically_typed)
ruby = add_url(
    name='Ruby',
    url='https://www.ruby-lang.org/en/',
).link(programming_language, dynamically_typed, object_oriented_programming, functional_programming)
prolog = add_node(name='Prolog').link(programming_language, dynamically_typed, logic_programming)
python = add_url(
    name='Python',
    url='https://www.python.org/',
).link(programming_language, dynamically_typed)
go = add_url(
    name='Go',
    url='https://go.dev/',
).link(programming_language, statically_typed, concurrent_programming)
java = add_node(name='Java').link(programming_language, statically_typed, object_oriented_programming)
common_lisp = add_url(
    name='Common Lisp',
    url='https://common-lisp.net/'
).link(programming_language, dynamically_typed, functional_programming)
rust = add_url(
    name='Rust',
    url='https://www.rust-lang.org/',
).link(programming_language, statically_typed, functional_programming)
scala = add_url(
    name='Scala',
    url='https://www.scala-lang.org/'
).link(programming_language, statically_typed, functional_programming, object_oriented_programming)
clojure = add_url(
    name='Clojure',
    url='https://clojure.org/'
).link(programming_language, dynamically_typed, functional_programming)
ocaml = add_url(
    name='OCaml',
    url='https://ocaml.org/'
).link(programming_language, statically_typed, functional_programming, object_oriented_programming)
coq = add_node(
    name='Coq',
    url='https://coq.inria.fr/',
).link(proof_assistant, programming_language, statically_typed, functional_programming)
racket = add_url(
    name='Racket',
    url='https://racket-lang.org/',
).link(programming_language, dynamically_typed, functional_programming)
oz = add_url(
    name='Oz',
    url='https://en.wikipedia.org/wiki/Oz_(programming_language)',
).link(programming_language, dynamically_typed, functional_programming, object_oriented_programming, logic_programming, concurrent_programming)
kotlin = add_url(
    name='Kotlin',
    url='https://kotlinlang.org/'
).link(programming_language, statically_typed, functional_programming, object_oriented_programming)
erlang = add_url(
    name='Erlang',
    url='https://www.erlang.org/',
).link(programming_language, dynamically_typed, functional_programming, concurrent_programming)
elixir = add_node(
    name='Elixir',
    url='https://elixir-lang.org/',
).link(programming_language, dynamically_typed, functional_programming, concurrent_programming)
assembly = add_node(name='Assembly').link(programming_language)
fsharp = add_url(
    name='F#',
    url='https://fsharp.org/'
).link(programming_language, statically_typed, object_oriented_programming, functional_programming)
swift = add_url(
    name='Swift',
    url='https://developer.apple.com/swift/'
).link(programming_language, statically_typed)
zig = add_url(
    name='Zig',
    url='https://ziglang.org/',
).link(programming_language, statically_typed)
dart = add_url(
    name='Dart',
    url='https://dart.dev/'
).link(programming_language, statically_typed, object_oriented_programming, functional_programming)
php = add_url(
    name='PHP',
    url='https://www.php.net/',
).link(programming_language, dynamically_typed)
raku = add_url(
    name='Raku',
    url='https://www.raku.org/',
).link(programming_language, object_oriented_programming, functional_programming)
css = add_node(name='CSS').link(frontend, webdev)
html = add_node(name='HTML').link(frontend, webdev)
sql = add_node(name='SQL').link(database)

jquery = add_url(
    name='jQuery',
    url='https://jquery.com/',
).link(library, javascript, typescript, webdev, frontend)

mysql = add_url(
    name='MySQL',
    url='https://www.mysql.com/',
).link(database)

angular = add_url(
    name='Angular',
    url='https://angular.io/'
).link(frontend, library, javascript, typescript, webdev)

vuejs = add_url(
    name='Vue.js',
    url='https://vuejs.org/',
).link(frontend, library, javascript, typescript, webdev)

react = add_url(
    name='React',
    url='https://reactjs.org/',
).link(frontend, library, javascript, typescript, webdev)

github = add_url(
    name='GitHub',
    url='https://github.com',
).link(git)

add_url(
    name='BitBucket',
    url='https://bitbucket.org',
).link(git)

add_url(
    name='GitLab',
    url='https://about.gitlab.com/',
).link(git)

add_url(
    name='Haskell Hierarchical Libraries',
    url="https://downloads.haskell.org/~ghc/latest/docs/html/libraries/index.html",
).link(haskell, library, reference)

add_url(
    name='Real World Haskell',
    url='http://book.realworldhaskell.org/read/',
).link(haskell, book, free)

add_url(
    name='Hoogle',
    description='Search Haskell libraries based on function names or type signatures',
    url="https://www.haskell.org/hoogle/",
).link(haskell, library, reference)

add_url(
    name="Don't fear the Monad",
    description="Accessible explanation of monads",
    url="https://channel9.msdn.com/Shows/Going+Deep/Brian-Beckman-Dont-fear-the-Monads",
).link(haskell, monad, video, tutorial)

add_pdf(
    name='A Philosophy of Software Design',
    authors=['John Ousterhout'],
    filename='a-philosophy-of-software-design.zpaq',
).link(software_development, book)

add_pdf(
    name='Algebra of Programming',
    authors=['Richard Bird', 'Oege de Moor'],
    filename='algebra-of-programming.zpaq',
).link(software_development, book)

add_pdf(
    name='Advanced Programming Language Design',
    authors=['Raphael Finkel'],
    filename='advanced-programming-language-design.zpaq',
).link(programming_language, book)

add_pdf(
    name='Angular Up & Running',
    authors=['Shyam Seshadri'],
    filename='angular-up-and-running.zpaq',
).link(angular, webdev, frontend, book)

add_pdf(
    name='Beamer User Guide',
    authors=[],
    filename='angular-up-and-running.zpaq',
).link(latex, book, reference)

add_pdf(
    name='TeX By Topic',
    authors=['Victor Eijkhout'],
    filename='tex-by-topic.zpaq',
).link(latex, book, reference)

add_pdf(
    name='TikZ & PGF',
    authors=[],
    filename='tikz-pgf.zpaq',
).link(latex, book, reference)

add_pdf(
    name='Learning JavaScript',
    authors=['Ethan Brown'],
    filename='learning-javascript.zpaq',
).link(latex, book)

add_pdf(
    name='Git Internals',
    authors=['Scott Chacon'],
    filename='git-internals.zpaq',
).link(git, book)

add_pdf(
    name='Learning GraphQL',
    authors=['Eve Porcello', 'Alex Banks'],
    filename='learning-graphql.zpaq',
).link(git, book)

add_pdf(
    name='GitHub Essentials',
    authors=['Achilleas Pipinellis'],
    filename='github-essentials.zpaq',
).link(git, github, book)

add_pdf(
    name='Linux Bible',
    authors=['Christopher Negus'],
    filename='linux-bible.zpaq',
).link(linux, book)

add_pdf(
    name='Flask Web Development',
    authors=['Miguel Grinberg'],
    filename='flask-web-development.zpaq',
).link(python, flask, webdev, frontend)

add_pdf(
    name='Homotopy Type Theory',
    authors=[''],
    filename='homotopy-type-theory.zpaq',
).link(book, computer_science, type_system)

add_pdf(
    name='The Rust Programming Language',
    authors=['Steve Klabnik', 'Carol Nichols'],
    filename='rust-programming-language.zpaq',
).link(rust, book)

add_pdf(
    name='Assembly Language Step by Step',
    authors=['Jeff Duntemann'],
    filename='assembly-language-step-by-step.zpaq',
).link(assembly, book)

add_pdf(
    name='Beginning Linux Programming',
    authors=['Neil Matthew', 'Richard Stones'],
    filename='beginning-linux-programming.zpaq',
).link(linux, software_development, c, book)

add_pdf(
    name='Buliding Tools with GitHub',
    authors=['Chris Dawson'],
    filename='building-tools-with-github.zpaq',
).link(git, github, book)

add_pdf(
    name='Machine Learning',
    authors=['Tom M. Mitchell'],
    filename='machine-learning.zpaq',
).link(machine_learning, book)

add_pdf(
    name='Computer Architecture',
    authors=['John L. Hennessy', 'David A. Patterson'],
    filename='computer-architecture.zpaq',
).link(computer_architecture, book)

add_pdf(
    name='Linux Essentials',
    authors=['Christine Bresnahan', 'Richard Blum'],
    filename='linux-essentials.zpaq',
).link(linux, book)

add_pdf(
    name='Linux Server Security',
    authors=['Chris Binnie'],
    filename='linux-server-security.zpaq',
).link(linux, security, book)

add_pdf(
    name='CSS The Definitive Guide',
    authors=['Eric A. Meyer', 'Estelle Weyl'],
    filename='css-definitive-guide.zpaq',
).link(css, book)

add_pdf(
    name='Data Visualization with Python & JavaScript',
    authors=['Kyran Dale'],
    filename='data-visualization-with-python-and-javascript.zpaq',
).link(graphics, python, javascript, data, book)

add_pdf(
    name='High Performance Images',
    authors=['Colin Bendell', 'Tim Kadlec', 'Yoav Weiss', 'Guy Podjarny', 'Nick Doyle', 'Mike McCall'],
    filename='high-performance-images.zpaq',
).link(graphics, book)

add_pdf(
    name='Mastering Modular JavaScript',
    authors=['Nicolas Bevacqua'],
    filename='mastering-modular-javascript.zpaq',
).link(javascript, book)

add_pdf(
    name='CSS Pocket Reference',
    authors=['Eric A. Meyer'],
    filename='css-pocket-reference.zpaq',
).link(css, reference, book)

add_pdf(
    name='Ray Tracing Gems',
    authors=[''],
    filename='ray-tracing-gems-1.zpaq',
).link(raytracing, book)

add_pdf(
    name='Ray Tracing Gems II',
    authors=[''],
    filename='ray-tracing-gems-2.zpaq',
).link(raytracing, book)

add_pdf(
    name='The Art of Multiprocessor Programming',
    authors=['Maucice Herlihy', 'Nir Shavit'],
    filename='art-of-multiprocessor-programming.zpaq',
).link(parallelism, software_development, java, book)

add_pdf(
    name='Designing Web APIs',
    authors=['Brenda Jin', 'Saurabh Sahni', 'Amir Shevat'],
    filename='designing-web-apis.zpaq',
).link(webdev, book)

add_pdf(
    name='Digital Design and Computer Architecture',
    authors=['David Money Harris', 'Sarah L. Harris'],
    filename='digital-design-and-computer-architecture.zpaq',
).link(computer_architecture, book)

add_pdf(
    name='Lectures on Computation',
    authors=['Richard P. Feynman'],
    filename='lectures-on-computation.zpaq',
).link(book)

add_pdf(
    name='Linux All-In-One For Dummies',
    authors=['Emmett Dulaney'],
    filename='linux-all-in-one-for-dummies.zpaq',
).link(linux, book)

add_pdf(
    name='Linux Command Line and Shell Scripting Bible',
    authors=['Richard Blum', 'Christine Bresnahan'],
    filename='linux-command-line-and-shell-scripting-bible.zpaq',
).link(linux, shell_scripting, book)

add_pdf(
    name='The Microarchitecture of Intel, AMD and VIA CPUs',
    authors=['Agner Fog'],
    filename='microarchitecture-of-intel-amd-and-via-cpus.zpaq',
).link(linux, book)

add_pdf(
    name='The Mystery of Banking',
    authors=['Murray N. Rothbard'],
    filename='mystery-of-banking.zpaq',
).link(economics, book)

add_pdf(
    name='Professional Linux Kernel Architecture',
    authors=['Wolfgang Mauerer'],
    filename='professional-linux-kernel-architecture.zpaq',
).link(linux, book)

add_pdf(
    name='Shell Scripting',
    authors=['Steve Parker'],
    filename='shell-scripting.zpaq',
).link(linux, shell_scripting, book)

add_pdf(
    name='The UNIX-Haters Handbook',
    authors=[''],
    filename='unix-haters-handbook.zpaq',
).link(unix, book)

add_pdf(
    name='Implementing Functional Languages',
    authors=['Simon Peyton Jones'],
    filename='implementing-functional-languages.zpaq',
).link(programming_language, computer_science, functional_programming, book)

add_pdf(
    name='Implementation of Functional Languages',
    authors=['Simon Peyton Jones'],
    filename='implementation-of-functional-languages.zpaq',
).link(programming_language, computer_science, functional_programming, book)

add_pdf(
    name='Learning PHP, MySQL & JavaScript',
    authors=['Robin Nixon'],
    filename='learning-php-mysql-and-javascript.zpaq',
).link(php, mysql, javascript, css, html, jquery, book)

add_pdf(
    name='Patterns of Enterprise Application Architecture',
    authors=['Martin Fowler'],
    filename='patterns-of-enterprise-application-architecture.zpaq',
).link(software_development, book)

add_pdf(
    name='RESTful Web Services',
    authors=['Leonard Richardson', 'Sam Ruby'],
    filename='restful-web-services.zpaq',
).link(rest, webdev, book)

add_pdf(
    name='Vue.js Up and Running',
    authors=['Callum Macrae'],
    filename='vuejs_up-and-running.zpaq',
).link(vuejs, book)

add_pdf(
    name='Principles of Programming Languages',
    authors=['Bruce J. MacLennan'],
    filename='principles-of-programming-languages.zpaq',
).link(programming_language, computer_science, book)

add_pdf(
    name='Programming Languages: Application and Interpretation',
    authors=['Shriram Krishnamurthi'],
    filename='programming-languages-application-and-interpretation.zpaq',
).link(programming_language, computer_science, book)

add_pdf(
    name='A Survey of Porgramming Language Memory Models',
    authors=['Evgenii Moiseenko', 'Anton Podkopaev', 'Dmitrii Koznov'],
    filename='memory-models-survey.zpaq',
).link(computer_science, book)

add_pdf(
    name='What Every Programmer Should Know About Memory',
    authors=['Ulrich Drepper'],
    filename='what-every-programmer-should-know-about-memory.zpaq',
).link(computer_science, book)

add_pdf(
    name='Testing Python: Applying Unit Testing, TDD, BDD and Acceptance Testing',
    authors=['David Sale'],
    filename='testing-python.zpaq',
).link(python, unit_testing, tdd, bdd, book)

add_pdf(
    name='Ubuntu Linux Toolbox',
    authors=['Christopher Negus'],
    filename='ubuntu-linux-toolbox.zpaq',
).link(linux, book)

add_pdf(
    name='The Room Where It Happened',
    authors=['John Bolton'],
    filename='the-room-where-it-happened.zpaq',
).link(politics, book)

add_pdf(
    name='CompTIA Linux+ and LPIC Practice Tests',
    authors=[''],
    filename='linux-practice-tests.zpaq',
).link(linux, book)

add_pdf(
    name='CompTIA Linux+ Study Guide (Exams LX0-103,)',
    authors=['Christine Bresnahan', 'Richard Blum'],
    filename='linux-study-guide.zpaq',
).link(linux, book)

add_pdf(
    name='Red Hat Enterprise Linux 6 Administration',
    authors=[''],
    filename='redhat-enterprise-linux6-administration.zpaq',
).link(linux, book)

add_pdf(
    name="You Don't Know JS: ES6 & Beyond",
    authors=['Kyle Simpson'],
    filename='es6-and-beyond.zpaq',
).link(javascript, book)

add_pdf(
    name="You Don't Know JS: Up and Going",
    authors=['Kyle Simpson'],
    filename='up-and-going.zpaq',
).link(javascript, book)

add_pdf(
    name="You Don't Know JS: Scope & Closures",
    authors=['Kyle Simpson'],
    filename='scope-and-closures.zpaq',
).link(javascript, book)

add_pdf(
    name='LPIC-1 Study Guide (Exams 101-400, 102-400)',
    authors=['Christine Bresnahan', 'Richard Blum'],
    filename='lpic1-study-guide.zpaq',
).link(linux, book)

add_pdf(
    name='LPIC-2 Study Guide (Exams 201, 202)',
    authors=['Christine Bresnahan', 'Richard Blum'],
    filename='lpic1-study-guide.zpaq',
).link(linux, book)

add_pdf(
    name='Raiders of the Lost Ark - Story Conference Transcript',
    authors=['George Lucas', 'Steven Spielberg', 'Larry Kasdan'],
    filename='raiders-of-the-lost-ark-story-conference-transcript.zpaq',
).link(movie)

add_url(
    name='Practical Common Lisp',
    authors=['Peter Seibel'],
    url='https://gigamonkeys.com/book/'
).link(free, book, common_lisp)

add_url(
    name='Pro Git',
    authors=['Scott Chacon', 'Ben Straub'],
    url='https://git-scm.com/book/en/v2'
).link(free, book, git)

add_url(
    name='Learn Git Branching',
    url='https://learngitbranching.js.org/'
).link(tutorial, git)

add_url(
    name='Practical Go: Real world advice for writing maintainable Go programs',
    url='https://dave.cheney.net/practical-go/presentations/qcon-china.html',
    authors=['Dave Cheney'],
).link(go, book)

add_url(
    name='Styled Components',
    url='https://www.styled-components.com/',
    description='Library for styling React components'
).link(javascript, typescript, webdev, react, library)

add_url(
    name='Material UI',
    url='https://material-ui.com/',
    description='Library of React components'
).link(javascript, typescript, webdev, react, library)

add_pdf(
    name='Active Learning',
    authors=['Burr Settles'],
    filename='active-learning.zpaq',
).link(ai, book)

add_pdf(
    name='Adversarial Machine Learning',
    authors=['Yevgeniy Vorobeychik', 'Murat Kantarcioglu'],
    filename='adversarial-machine-learning.zpaq',
).link(ai, book)

add_pdf(
    name='A Guide to Convolutional Neural Networks for Computer Vision',
    authors=['Salman Khan', 'Hossein Rahmani', 'Syed Afaq Ali Shah', 'Mohammed Bennamoun'],
    filename='a-guide-to-convolutional-neural-networks-for-computer-vision.zpaq',
).link(ai, book)

add_pdf(
    name='Algorithms for Reinforcement Learning',
    authors=['Csaba Szepesvari'],
    filename='algorithms-for-reinforcement-learning.zpaq',
).link(ai, book)

add_pdf(
    name='Covariances in Computer Vision and Machine Learning',
    authors=['Ha Quang Minh', 'Vittorio Murino'],
    filename='covariances-in-computer-vision-and-machine-learning.zpaq',
).link(ai, book)

add_pdf(
    name='Creating Autonomous Vehicle Systems',
    authors=['Shaoshan Liu', 'Liyun Li', 'Jie Tang', 'Shuang Wu', 'Jean-Luc Gaudiot'],
    filename='creating-autonomous-vehicle-systems.zpaq',
).link(ai, book)

add_pdf(
    name='Data-IntensiveText Processing with MapReduce',
    authors=['Jimmy Lin', 'Chris Dyer'],
    filename='data-intensive-text-processing-with-mapreduce.zpaq',
).link(ai, book)

add_pdf(
    name='Data Managementin Machine Learning Systems',
    authors=['Matthias Boehm', 'Arun Kumar', 'Jun Yang'],
    filename='data-management-in-machine-learning-systems.zpaq',
).link(ai, book)

add_pdf(
    name='Detecting FakeNews on Social Media',
    authors=['Kai Shu', 'Huan Liu'],
    filename='detecting-fake-news-on-social-media.zpaq',
).link(ai, book)

add_pdf(
    name='Essentials of Game Theory',
    authors=['Kevin Leyton-Brown', 'Yoav Shoham'],
    filename='detecting-fake-news-on-social-media.zpaq',
).link(ai, book)

add_pdf(
    name='Human Computation',
    authors=['Edith Law', 'Luis von Ahn'],
    filename='human-computation.zpaq',
).link(ai, book)

add_pdf(
    name='Introduction to Intelligent Systems in Traffic and Transportation',
    authors=['Ana L.C. Bazzan', 'Franziska Klügl'],
    filename='introduction-to-intelligent-systems-in-traffic-and-transportation.zpaq',
).link(ai, book)

add_pdf(
    name='Introduction to Semi-Supervised Learning',
    authors=['Xiaojin Zhu', 'Andrew B. Goldberg'],
    filename='introduction-to-semi-supervised-learning.zpaq',
).link(ai, book)

add_pdf(
    name='Lifelong Machine Learning',
    authors=['Zhiyuan Chen', 'Bing Liu'],
    filename='lifelong-machine-learning.zpaq',
).link(ai, book)

add_pdf(
    name='Metric Learning',
    authors=['Aurelien Bellet', 'Amaury Habrard', 'Marc Sebban'],
    filename='metric-learning.zpaq',
).link(ai, book)

add_pdf(
    name='Natural Language Processing for Social Media',
    authors=['Atefeh Farzindar', 'Diana Inkpen'],
    filename='natural-language-processing-for-social-media.zpaq',
).link(ai, book)

add_pdf(
    name='Neural Network Methods for Natural Language Processing',
    authors=['Yoav Goldberg'],
    filename='neural-network-methods-for-natural-language-processing.zpaq',
).link(ai, book)

add_pdf(
    name='Sentiment Analysis and Opinion Mining',
    authors=['Bing Liu'],
    filename='sentiment-analysis-and-opinion-mining.zpaq',
).link(ai, book)

add_pdf(
    name='Statistical Relational Artificial Intelligence',
    authors=['Luc De Raedt', 'Kristian Kersting', 'Sriraam Natarajan', 'David Poole'],
    filename='statistical-relational-artificial-intelligence.zpaq',
).link(ai, book)

add_pdf(
    name='Applied Cryptography',
    authors=['Bruce Schneier'],
    filename='applied-cryptography-protocols-algorithms-and-source-code-in-c.zpaq'
).link(security, book)

add_pdf(
    name='Art of Intrusion',
    authors=['Kevin D. Mitnick', 'William L. Simon'],
    filename='art-of-intrusion.zpaq'
).link(security, book)

add_pdf(
    name='The Art of Memory Forensics',
    authors=['Michael Hale Ligh', 'Andrew Case', 'Jamie Levy',' Aaron Walters'],
    filename='art-of-memory-forensics-detecting-malware-and-threats-in-windows-linux-and-mac-memory.zpaq'
).link(security, book)

add_pdf(
    name='Cryptography Engineering',
    authors=['Niels Ferguson', 'Bruce Schneier', 'Tadayoshi Kohno'],
    filename='cryptography-engineering-design-principles-and-practical-applications.zpaq'
).link(security, book)

add_pdf(
    name='Liars and Outliers',
    authors=['Bruce Schneier'],
    filename='liarsandoutliers-enablingthetrustthatsocietyneedstothrive.zpaq'
).link(security, book)

add_pdf(
    name="Malware Analyst’s Cookbook and DVD",
    authors=['Michael Hale Ligh', 'Steven Adair', 'Blake Hartstein', 'Matthew Richard'],
    filename='malware-analysts-cookbook-and-dvd-tools-and-techniques-for-fighting-malicious-code.zpaq'
).link(security, book)

add_pdf(
    name='Practical Reverse Engineering',
    authors=['Bruce Dang', 'Alexandre Gazet', 'Elias Bachaalany'],
    filename='practical-reverse-engineering-x86-x64-arm-windows-kernel-reversing-tools-and-obfuscation.zpaq'
).link(security, book)

add_pdf(
    name='Secrets and Lies',
    authors=['Bruce Schneier'],
    filename='secrets-and-lies-digital-security-in-a-networked-world.zpaq'
).link(security, book)

add_pdf(
    name="The Shellcoder’s Handbook",
    authors=['Chris Anley', 'John Heasman', 'Felix Linder', 'Gerardo Richarte'],
    filename='shellcoders-handbook-discovering-and-exploiting-security-holes.zpaq'
).link(security, book)

add_pdf(
    name='Social Engineering',
    authors=['Christopher Hadnagy'],
    filename='social-engineering-the-science-of-human-hacking.zpaq'
).link(security, book)

add_pdf(
    name='The Art of Deception',
    authors=['Kevin D. Mitnick', 'William L. Simon'],
    filename='the-art-of-deception-controlling-the-human-element-of-security.zpaq'
).link(security, book)

add_pdf(
    name='Threat Modeling',
    authors=['Adam Shostack'],
    filename='threat-modeling-designing-for-security.zpaq'
).link(security, book)

add_pdf(
    name='Unauthorised Access',
    authors=['Wil Allsopp: Physical Penetration Testing For IT Security Teams'],
    filename='unauthorised-access-physical-penetration-testing-for-it-security-teams.zpaq'
).link(security, book)

add_pdf(
    name='We Have Root: Even More Advice from Schneier on Security',
    authors=['Bruce Schneier'],
    filename='we-have-root-even-more-advice-from-schneier-on-security.zpaq'
).link(security, book)

add_pdf(
    name='The Web Application Hacker’s Handbook',
    authors=['Dafydd Stuttard', 'Marcus Pinto'],
    filename='web-application-hackers-handbook-finding-and-exploiting-security-flaws.zpaq'
).link(security, book)

add_pdf(
    name='Agile Project Management with Azure DevOps',
    authors=['Joachim Rossberg'],
    filename='agile-project-management-with-azure-devops.zpaq'
).link(azure, book, devops)

add_pdf(
    name='Azure Arc-Enabled Data Services Revealed',
    authors=['Ben Weissman', 'Anthony E. Nocentino'],
    filename='azure-arc-enabled-dataservices-revealed.zpaq'
).link(azure, book)

add_pdf(
    name='Azure Internet of Things Revealed',
    authors=['Robert Stackowiak'],
    filename='azure-internet-of-things-revealed.zpaq'
).link(azure, book)

add_pdf(
    name='Azure Serverless Computing Cookbook',
    authors=['Praveen Kumar Sreeram'],
    filename='azure-serverless-computing-cookbook.zpaq'
).link(azure, book)

add_pdf(
    name='Azure SQL Revealed',
    authors=['Bob Ward'],
    filename='azure-sql-revealed.zpaq'
).link(azure, book, sql)

add_pdf(
    name='Beginning Azure Functions',
    authors=['Rahul Sawhney'],
    filename='beginning-azure-functions.zpaq'
).link(azure, book)

add_pdf(
    name='Beginning Azure IoT Edge Computing',
    authors=['David Jensen'],
    filename='beginning-azure-iot-edge-computing.zpaq'
).link(azure, book)

add_pdf(
    name='Building Microservices Applications on Microsoft Azure',
    authors=['Harsh Chawla', 'Hemant Kathuria'],
    filename='building-microservices-applications-on-microsoft-azure.zpaq'
).link(azure, book, microservice)

add_pdf(
    name='Cloud Debugging and Profiling in Microsoft Azure',
    authors=['Jeffrey Chilberto', 'Sjoukje Zaal', 'Gaurav Aroraa', 'Ed Price'],
    filename='cloud-debugging-and-profiling-in-microsoft-azure.zpaq'
).link(azure, book)

add_pdf(
    name='Cyber Security on Azure',
    authors=['Marshall Copeland'],
    filename='cybersecurity-on-azure.zpaq'
).link(azure, book, security)

add_pdf(
    name='Developing Applications with Azure Active Directory',
    authors=['Manas Mayank', 'Mohit Garg'],
    filename='developing-applications-with-azure-active-directory.zpaq'
).link(azure, book)

add_pdf(
    name='DevOps for Azure Applications',
    authors=['Suren Machiraju', 'Suraj Gaurav'],
    filename='devops-for-azure-applications.zpaq'
).link(azure, book, devops)

add_pdf(
    name='Getting Started with Containers in Azure',
    authors=['Shimon Ifrah'],
    filename='getting-started-with-containers-in-azure.zpaq'
).link(azure, book)

add_pdf(
    name='Hands-on Azure Pipelines',
    authors=['Chaminda Chandrasekara', 'Pushpa Herath'],
    filename='hands-on-azure-pipelines.zpaq'
).link(azure, book)

add_pdf(
    name='Hands-on Azure Repos',
    authors=['Chaminda Chandrasekara', 'Pushpa Herath'],
    filename='hands-on-azure-repos.zpaq'
).link(azure, book)

add_pdf(
    name='Hardening Azure Applications',
    authors=['Suren Machiraju', 'Suraj Gaurav'],
    filename='hardening-azure-applications.zpaq'
).link(azure, book)

add_pdf(
    name='Introducing Azure Bot Service',
    authors=['Charles Waghmare'],
    filename='introducing-azure-bot-service.zpaq'
).link(azure, book)

add_pdf(
    name='Introducing Azure Kubernetes Service',
    authors=['Steve Buchanan', 'Janaka Rangama', 'Ned Bellavance'],
    filename='introducing-azure-kubernetes-service.zpaq'
).link(azure, book)

add_pdf(
    name='Introducing Disaster Recovery with Microsoft Azure',
    authors=['Bapi Chakraborty', 'Yashajeet Chowdhury'],
    filename='introducing-disaster-recovery-with-microsoft-azure.zpaq'
).link(azure, book)

add_pdf(
    name='Microsoft Azure Cosmos DB Revealed',
    authors=['Jose Rolando Guay Paz'],
    filename='microsoft-azure-cosmos-db-revealed.zpaq'
).link(azure, book, database)

add_pdf(
    name='Microsoft Azure: Planning, Deploying, and Managing the Cloud',
    authors=['Julian Soh', 'Marshall Copeland', 'Anthony Puca', 'Micheleen Harris'],
    filename='microsoft-azure.zpaq'
).link(azure, book)

add_pdf(
    name='Migrating a Two-Tier Application to Azure',
    authors=['Peter De Tender'],
    filename='migrating-a-two-tier-application-to-azure.zpaq'
).link(azure, book)

add_pdf(
    name='Migrating to Azure',
    authors=['Josh Garverick'],
    filename='migrating-to-azure.zpaq'
).link(azure, book)

add_pdf(
    name='The Modern Data Warehouse in Azure',
    authors=['Matt How'],
    filename='modern-data-warehouse-in-azure.zpaq'
).link(azure, book)

add_pdf(
    name='Practical Azure Functions: A Guide to Web, Mobile, and IoT Applications',
    authors=['Agus Kurniawan Wely Lau'],
    filename='practical-azure-functions.zpaq'
).link(azure, book)

add_pdf(
    name='Practical Azure SQL Database for Modern Developers',
    authors=['Davide Mauri', 'Silvano Coriani', 'Anna Hoffman', 'Sanjay Mishra', 'Jovan Popovic'],
    filename='practical-azure-sql-database-for-modern-developers.zpaq'
).link(azure, book, sql)

add_pdf(
    name='Practical Microsoft Azure IaaS',
    authors=['Shijimol Ambi Karthikeyan'],
    filename='practical-microsoft-azure-iaas.zpaq'
).link(azure, book)

add_pdf(
    name='Pro Azure Governance and Security',
    authors=['Peter De Tender', 'David Rendon', 'Samuel Erskine'],
    filename='pro-azure-governance-and-security.zpaq'
).link(azure, book, security)

add_pdf(
    name='Understanding Azure Data Factory: Operationalizing Big Data and Advanced Analytics Solutions',
    authors=['Sudhir Rawat', 'Abhishek Narain'],
    filename='understanding-azure-data-factory.zpaq'
).link(azure, book)

add_pdf(
    name='Understanding Azure Monitoring',
    authors=['Bapi Chakraborty', 'Shijimol Ambi Karthikeyan'],
    filename='understanding-azure-monitoring.zpaq'
).link(azure, book)

add_pdf(
    name='Web Applications on Azure',
    authors=['Rob Reagan'],
    filename='web-applications-on-azure.zpaq'
).link(azure, book, webdev)
