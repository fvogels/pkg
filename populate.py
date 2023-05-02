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


def add_pdf(*, name, filename, **kwargs):
    return add_node(
        name=name,
        protocol='pdf',
        filename=filename,
        **kwargs,
    )


def link(from_node, to_node):
    filter = {'_id': from_node}
    update = { '$addToSet': { 'links': to_node } }
    graph.update_one(filter, update)


math = add_node(name='Mathematics')
algebra = add_node(name='Algebra').link(math)
linear_algebra = add_node(name='Linear Algebra').link(algebra)
topology = add_node(name='Topology').link(math)
science = add_node(name='Science')
physics = add_node(name='Physics').link(science)
software_development = add_node(name='Software Development')
gamedev = add_node(name='Game Development')
mobiledev = add_node(name='Mobile Development')
quantum = add_node(name='Quantum')
networks = add_node(name='Networks')
programming_language = add_node(name='Programming Language').link(software_development)
proof_assistant = add_node(name='Proof Assistant').link(math)
functional_programming = add_node(name='Functional Programming')
object_oriented_programming = add_node(name='Object Oriented Programming')
concurrent_programming = add_node(name='Concurrent Programming')
distributed_computing = add_node(name='Distributed Computing')
cloud = add_node(name='Cloud Development')
logic_programming = add_node(name='Logic Programming')
type_system = add_node(name='Type System').link(programming_language)
dynamically_typed = add_node(name='Dynamic Typing').link(type_system)
statically_typed = add_node(name='Static Typing').link(type_system)
dependent_typing = add_node(name='Dependent Typing').link(type_system)
computer_science = add_node(name='Computer Science')
webdev = add_node(name='Web Development').link(software_development)
frontend = add_node(name='Front End')
backend = add_node(name='Back End')
latex = add_node(name='LaTeX')
git = add_node(name='Git')
linux = add_node(name='Linux')
unix = add_node(name='Unix')
ai = add_node(name='Artificial Intelligence')
nlp = add_node(name='Natural Language Processing').link(ai)
iot = add_node(name='Internet of Things')
machine_learning = add_node(name='Machine Learning').link(ai)
computer_architecture = add_node(name='Computer Architecture')
security = add_node(name='Security')
database = add_node(name='Database')
data = add_node(name='Data Science')
graphics = add_node(name='Graphics')
raytracing = add_node(name='Ray Tracing').link(graphics)
parallelism = add_node(name='Parallelism').link(graphics)
economics = add_node(name='Economics')
politics = add_node(name='Politics')
shell_scripting = add_node(name='Shell Scripting')
rest = add_node(name='REST')
testing = add_node(name='Testing')
unit_testing = add_node(name='Unit Testing').link(testing)
tdd = add_node(name='Test Driven Development').link(testing)
bdd = add_node(name='Behavior Driven Development').link(testing)
azure = add_node(name='Azure').link(cloud)
devops = add_node(name='DevOps')
ssh = add_node(name='SSH')
microservice = add_node(name='Microservice').link(distributed_computing)
excel = add_node(name='Excel')

software = add_node(name='Software')
editor = add_node(name='Editor')
ide = add_node(name='IDE')
library = add_node(name='Library')
framework = add_node(name='Framework')
book = add_node(name='Book')
free = add_node(name='Free')
reference = add_node(name='Reference')
monad = add_node(name='Monad')
video = add_node(name='Video')
tutorial = add_node(name='Tutorial')
virtualization = add_node(name='Virtualization')
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
).link(programming_language, dynamically_typed, functional_programming, concurrent_programming, distributed_computing)
elixir = add_node(
    name='Elixir',
    url='https://elixir-lang.org/',
).link(programming_language, dynamically_typed, functional_programming, concurrent_programming, distributed_computing)
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
nosql = add_node(name='NoSQL').link(database)

scipy = add_url(
    name='SciPy',
    url='https://scipy.org/',
).link(library, python, science)

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

react_native = add_url(
    name='React Native',
    url='https://reactnative.dev/',
).link(frontend, library, javascript, typescript, mobiledev)

android = add_url(
    name='Android',
    url='https://www.android.com/',
).link(mobiledev)

ios = add_url(
    name='iOS',
    url='https://www.apple.com/ios//',
).link(mobiledev)

flutter = add_url(
    name='Flutter',
    url='https://flutter.dev/',
).link(dart, framework)

xamarin = add_url(
    name='Xamarin',
    url='https://dotnet.microsoft.com/en-us/apps/xamarin',
).link()

ionic = add_url(
    name='Ionic',
    url='https://ionicframework.com/',
).link()

flask = add_url(
    name='Flask',
    url='https://flask.palletsprojects.com/',
).link(backend, framework, webdev, python)

django = add_url(
    name='Django',
    url='https://www.djangoproject.com/',
).link(framework, webdev, python)

scikit = add_url(
    name='SciKit',
    url='https://scikit-learn.org/stable/',
).link(python, library, science)

asterisk = add_url(
    name='Asterisk',
    url='https://www.asterisk.org/',
)

cassandra = add_url(
    name='Cassandra',
    url='https://cassandra.apache.org/',
).link(nosql)

cloud_foundry = add_url(
    name='Cloud Foundry',
    url='https://www.cloudfoundry.org/',
).link(cloud)

elastic_search = add_url(
    name='Elastic Search',
    url='https://www.elastic.co/',
).link(data)

bigquery = add_url(
    name='BigQuery',
    url='https://cloud.google.com/bigquery',
).link(data)

hadoop = add_url(
    name='Hadoop',
    url='https://hadoop.apache.org/',
).link(distributed_computing)

kafka = add_url(
    name='Kafka',
    url='https://kafka.apache.org/intro',
).link(distributed_computing)

maven = add_url(
    name='Maven',
    url='https://maven.apache.org/',
)

mongodb = add_url(
    name='MongoDB',
    url='https://www.mongodb.com/',
).link(nosql)

spark = add_url(
    name='Spark',
    url='https://spark.apache.org/',
).link(data)

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
).link(angular, book)

add_pdf(
    name='Beamer User Guide',
    filename='angular-up-and-running.zpaq',
).link(latex, book, reference)

add_pdf(
    name='TeX By Topic',
    authors=['Victor Eijkhout'],
    filename='tex-by-topic.zpaq',
).link(latex, book, reference)

add_pdf(
    name='TikZ & PGF',
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
).link(github, book)

add_pdf(
    name='Linux Bible',
    authors=['Christopher Negus'],
    filename='linux-bible.zpaq',
).link(linux, book)

add_pdf(
    name='Flask Web Development',
    authors=['Miguel Grinberg'],
    filename='flask-web-development.zpaq',
).link(flask, book)

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
    name='Building Tools with GitHub',
    authors=['Chris Dawson'],
    filename='building-tools-with-github.zpaq',
).link(github, book)

add_pdf(
    name='Machine Learning (book)',
    authors=['Tom M. Mitchell'],
    filename='machine-learning.zpaq',
).link(machine_learning, book)

add_pdf(
    name='Computer Architecture (book)',
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
    name='Shell Scripting (book)',
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
).link(php, mysql, css, html, jquery, book)

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
).link(react)

add_url(
    name='Material UI',
    url='https://material-ui.com/',
    description='Library of React components'
).link(react)

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
).link(azure, book, iot)

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
).link(azure, book, iot, mobiledev)

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

add_pdf(
    name='Applied Computational Thinking With Python',
    filename='applied-computational-thinking-with-python.zpaq',
).link(python, book)

add_pdf(
  name='Applying Math With Python',
  filename='applying-math-with-python.zpaq',
).link(python, book, math)

add_pdf(
  name='Artificial Intelligence With Python',
  filename='artificial-intelligence-with-python.zpaq',
).link(python, book, ai)

add_pdf(
  name='Automate The Boring Stuff With Python',
  filename='automate-the-boring-stuff-with-python.zpaq',
).link(python, book)

add_pdf(
  name='Beyond The Basic Stuff With Python',
  filename='beyond-the-basic-stuff-with-python.zpaq',
).link(python, book)

add_pdf(
  name='Black Hat Python',
  filename='black-hat-python.zpaq',
).link(python, book, security)

add_pdf(
  name='Cracking Codes With Python',
  filename='cracking-codes-with-python.zpaq',
).link(python, book, security)

add_pdf(
  name='Data Engineering With Python',
  filename='data-engineering-with-python.zpaq',
).link(python, book, data)

add_pdf(
  name='Deep Reinforcement Learning With Python',
  filename='deep-reinforcement-learning-with-python.zpaq',
).link(python, book, ai)

add_pdf(
  name='Django 3 By Example',
  filename='django3-by-example.zpaq',
).link(book, django)

add_pdf(
  name='Doing Math With Python',
  filename='doing-math-with-python.zpaq',
).link(python, book, math)

add_pdf(
  name='Elegant SciPy',
  filename='elegant-scipy.zpaq',
).link(book, scipy)

add_pdf(
  name='Fluent Python',
  filename='fluent-python.zpaq',
).link(python, book)

add_pdf(
  name='Gray Hat Python',
  filename='gray-hat-python.zpaq',
).link(python, book, security)

add_pdf(
  name='Hands On Exploratory Data Analysis With Python',
  filename='hands-on-exploratory-data-analysis-with-python.zpaq',
).link(python, book, data)

add_pdf(
  name='Hands On Genetic Algorithms With Python',
  filename='hands-on-genetic-algorithms-with-python.zpaq',
).link(python, book, ai)

add_pdf(
  name='Hands On Machine Learning With Scikit',
  filename='hands-on-machine-learning-with-scikit.zpaq',
).link(book, machine_learning, scikit)

add_pdf(
  name='Hands On Natural Language Processing With Python',
  filename='hands-on-natural-language-processing-with-python.zpaq',
).link(python, book, nlp)

add_pdf(
  name='Hands On Simulation Modeling With Python',
  filename='hands-on-simulation-modeling-with-python.zpaq',
).link(python, book)

add_pdf(
  name='Impractical Python Projects',
  filename='impractical-python-projects.zpaq',
).link(python, book)

add_pdf(
  name='Introducing Python',
  filename='introducing-python.zpaq',
).link(python, book)

add_pdf(
  name='Invent Your Own Computer Games With Python',
  filename='invent-your-own-computer-games-with-python.zpaq',
).link(python, book, gamedev)

add_pdf(
  name='Learn Quantum Computing With Python And IBM Quantum Experience',
  filename='learn-quantum-computing-with-python-and-ibm-quantum-experience.zpaq',
).link(python, book, quantum)

add_pdf(
  name='Learn To Program With Minecraft',
  filename='learn-to-program-with-minecraft.zpaq',
).link(python, book, gamedev)

add_pdf(
  name='Mastering Python Networking',
  filename='mastering-python-networking.zpaq',
).link(python, book, networks)

add_pdf(
  name='Math Adventures With Python',
  filename='math-adventures-with-python.zpaq',
).link(python, book, math)

add_pdf(
  name='Mission Python',
  filename='mission-python.zpaq',
).link(python, book)

add_pdf(
  name='Modern Python Cookbook',
  filename='modern-python-cookbook.zpaq',
).link(python, book)

add_pdf(
  name='Natural Language Processing With Python And Spacy',
  filename='natural-language-processing-with-python-and-spacy.zpaq',
).link(python, book, nlp)

add_pdf(
  name='Natural Language Processing With Python',
  filename='natural-language-processing-with-python.zpaq',
).link(python, book, nlp)

add_pdf(
  name='Practical Python Programming For IoT',
  filename='practical-python-programming-for-iot.zpaq',
).link(python, book, iot)

add_pdf(
  name='Python Algorithmic Trading Cookbook',
  filename='python-algorithmic-trading-cookbook.zpaq',
).link(python, book, economics)

add_pdf(
  name='Python Automation Cookbook',
  filename='python-automation-cookbook.zpaq',
).link(python, book)

add_pdf(
  name='Python Crash Course',
  filename='python-crash-course.zpaq',
).link(python, book)

add_pdf(
  name='Python Data Cleaning Cookbook',
  filename='python-data-cleaning-cookbook.zpaq',
).link(python, book, data)

add_pdf(
  name='Python Data Science Handbook',
  filename='python-data-science-handbook.zpaq',
).link(python, book, data)

add_pdf(
  name='Python Feature Engineering Cookbook',
  filename='python-feature-engineering-cookbook.zpaq',
).link(python, book)

add_pdf(
  name='Python Flashcards',
  filename='python-flashcards.zpaq',
).link(python, book)

add_pdf(
  name='Python For Finance Cookbook',
  filename='python-for-finance-cookbook.zpaq',
).link(python, book, economics)

add_pdf(
  name='Python For Kids',
  filename='python-for-kids.zpaq',
).link(python, book)

add_pdf(
  name='Python Image Processing Cookbook',
  filename='python-image-processing-cookbook.zpaq',
).link(python, book)

add_pdf(
  name='Python One Liners',
  filename='python-one-liners.zpaq',
).link(python, book)

add_pdf(
  name='Python Playground Geeky Projects For The Curious Programmer',
  filename='python-playground-geeky-projects-for-the-curious-programmer.zpaq',
).link(python, book)

add_pdf(
  name='Python Workshop',
  filename='python-workshop.zpaq',
).link(python, book)

add_pdf(
  name='Real World Python',
  filename='real-world-python.zpaq',
).link(python, book)

add_pdf(
  name='Serious Python',
  filename='serious-python.zpaq',
).link(python, book)

add_pdf(
  name='Statistics And Calculus With Python Workshop',
  filename='statistics-and-calculus-with-python-workshop.zpaq',
).link(python, book, math)

add_pdf(
  name='Teach Your Kids To Code',
  filename='teach-your-kids-to-code.zpaq',
).link(python, book)

add_pdf(
  name='Test Driven Development With Python',
  filename='test-driven-development-with-python.zpaq',
).link(python, book, tdd)

add_pdf(
  name='The Hitchhikers Guide To Python',
  filename='the-hitchhikers-guide-to-python.zpaq',
).link(python, book)

add_pdf(
  name='Think Bayes',
  filename='think-bayes.zpaq',
).link(python, book, math)

add_pdf(
  name='Think Python',
  filename='think-python.zpaq',
).link(python, book)

add_pdf(
  name='Thoughtful Machine Learning With Python',
  filename='thoughtful-machine-learning-with-python.zpaq',
).link(python, book, machine_learning)

add_pdf(
  name='Twisted Network Programming Essentials',
  filename='twisted-network-programming-essentials.zpaq',
).link(python, book, networks)

add_pdf(
  name='Web Development With Django Cookbook',
  filename='web-development-with-django-cookbook.zpaq',
).link(book, django)

add_pdf(
  name='Web Scraping With Python',
  filename='web-scraping-with-python.zpaq',
).link(python, book, webdev)

add_pdf(
  name='20 Essential Games To Study',
  filename='20-essential-games-to-study.zpaq',
).link(book, gamedev)

add_pdf(
  name='Basics Of Game Design',
  filename='basics-of-game-design.zpaq',
).link(book, gamedev)

add_pdf(
  name='Buttonless Incredible Iphone And Ipad Games And The Stories Behind Them',
  filename='buttonless-incredible-iphone-and-ipad-games-and-the-stories-behind-them.zpaq',
).link(book, gamedev)

add_pdf(
  name='Comedy For Animators',
  filename='comedy-for-animators.zpaq',
).link(book, gamedev)

add_pdf(
  name='Digital Mayhem 3D Landscape Techniques',
  filename='digital-mayhem-3d-landscape-techniques.zpaq',
).link(book, gamedev)

add_pdf(
  name="Directing For Animation Everything You Didn't Learn In Art School",
  filename='directing-for-animation-everything-you-didnt-learn-in-art-school.zpaq',
).link(book, gamedev)

add_pdf(
  name='Game Design Theory',
  filename='game-design-theory.zpaq',
).link(book, gamedev)

add_pdf(
  name="Game Magic A Designer's Guide To Magic Systems In Theory And Practice",
  filename='game-magic-adesigners-guide-to-magic-systems-in-theory-and-practice.zpaq',
).link(book, gamedev)

add_pdf(
  name='Honoring The Code',
  filename='honoring-the-code.zpaq',
).link(book, gamedev)

add_pdf(
  name='Independent Animation: Developing Producing And Distributing Your Animated Films',
  filename='independent-animation-developing-producing-and-distributing-your-animated-films.zpaq',
).link(book, gamedev)

add_pdf(
  name='Learn To Play Designing Tutorials For Video Games',
  filename='learn-to-play-designing-tutorials-for-video-games.zpaq',
).link(book, gamedev)

add_pdf(
  name='On The Way To Fun An Emotion Based Approach To Successful Game Design',
  filename='on-the-way-to-fun-anemotion-based-approach-to-successful-game-design.zpaq',
).link(book, gamedev)

add_pdf(
  name='Punk Playthings: Provocations For 21st Century Game Makers',
  filename='punk-playthings-provocations-for-21st-century-game-makers.zpaq',
).link(book, gamedev)

add_pdf(
  name='Reverse Design Diablo Ii',
  filename='reverse-design-diablo-ii.zpaq',
).link(book, gamedev)

add_pdf(
  name='Story Telling For Interactive Digital Media And Video Games',
  filename='story-telling-for-interactive-digital-media-and-video-games.zpaq',
).link(book, gamedev)

add_pdf(
  name="The Animator's Eye: Adding Life To Animation With Timing, Layout, Design, Color And Sound",
  filename='the-animators-eye-adding-life-to-animation-with-timing-layout-design-color-and-sound.zpaq',
).link(book, gamedev)

add_pdf(
    name='Asterisk: The Definitive Guide',
    filename="asterisk-the-definitive-guide.zpaq",
).link(software_development, book, asterisk)

add_pdf(
    name='Cassandra: The Definitive Guide',
    filename="cassandra-the-definitive-guide.zpaq",
).link(software_development, book)

add_pdf(
    name='Cloud Foundry: The Definitive Guide',
    filename="cloud-foundry-the-definitive-guide.zpaq",
).link(software_development, book)

add_pdf(
    name='Elastic Search: The Definitive Guide',
    filename="elastic-search-the-definitive-guide.zpaq",
).link(software_development, book, elastic_search)

add_pdf(
    name='Ethernet: The Definitive Guide',
    filename="ethernet-the-definitive-guide.zpaq",
).link(software_development, book, networks)

add_pdf(
    name='Google BigQuery: The Definitive Guide',
    filename="google-big-query-the-definitive-guide.zpaq",
).link(software_development, book, bigquery)

add_pdf(
    name='Hadoop: The Definitive Guide',
    filename="hadoop-the-definitive-guide.zpaq",
).link(software_development, book, hadoop)

add_pdf(
    name='Java Performance: The Definitive Guide',
    filename="java-performance-the-definitive-guide.zpaq",
).link(software_development, book, java)

add_pdf(
    name='JavaScript: The Definitive Guide',
    filename="javascript-the-definitive-guide.zpaq",
).link(software_development, book, javascript)

add_pdf(
    name='Kafka: The Definitive Guide',
    filename="kafka-the-definitive-guide.zpaq",
).link(software_development, book, kafka)

add_pdf(
    name='Maven: The Definitive Guide',
    filename="maven-the-definitive-guide.zpaq",
).link(software_development, book)

add_pdf(
    name='MongoDB: The Definitive Guide',
    filename="mongodb-the-definitive-guide.zpaq",
).link(software_development, book, mongodb)

add_pdf(
    name='Spark: The Definitive Guide',
    filename="spark-the-definitive-guide.zpaq",
).link(software_development, book, spark)

add_pdf(
    name='SSH The Secure Shell: The Definitive Guide',
    filename="ssh-the-secure-shell-the-definitive-guide.zpaq",
).link(software_development, book, ssh)

add_pdf(
  name="Algebra Essentials",
  filename='algebra-essentials.zpaq',
).link(book, algebra)

add_pdf(
  name="Applied Linear Algebra And Optimization Using Matlab",
  filename='applied-linear-algebra-and-optimization-using-matlab.zpaq',
).link(book, linear_algebra)

add_pdf(
  name="Cluster Analysis And Data Mining",
  filename='cluster-analysis-and-data-mining.zpaq',
).link(book, math, data)

add_pdf(
  name="Commutative Algebra",
  filename='commutative-algebra.zpaq',
).link(book, algebra)

add_pdf(
  name="Cosmol Heat Transfer Models",
  filename='cosmol-heat-transfer-models.zpaq',
).link(book, math, physics)

add_pdf(
  name="Dimensional Analysis For Unit Conversion Using Matlab",
  filename='dimensional-analysis-for-unit-conversion-using-matlab.zpaq',
).link(book, math, physics)

add_pdf(
  name="Direct Energy Conversion Technologies",
  filename='direct-energy-conversion-technologies.zpaq',
).link(book, math, physics)

add_pdf(
  name="Essentials Of Modern Algebra",
  filename='essentials-of-modern-algebra.zpaq',
).link(book, algebra)

add_pdf(
  name="Finite Element Analysis",
  filename='finite-element-analysis.zpaq',
).link(book, math)

add_pdf(
  name="Flight Science",
  filename='flight-science.zpaq',
).link(book, math, science)

add_pdf(
  name="Foundations Of Math",
  filename='foundations-of-math.zpaq',
).link(book, math)

add_pdf(
  name="Foundations Of Physics",
  filename='foundations-of-physics.zpaq',
).link(book, math, physics)

add_pdf(
  name="Geometry Creation And Import",
  filename='geometry-creation-and-import.zpaq',
).link(book, math)

add_pdf(
  name="Linear Algebra (book)",
  filename='linear-algebra.zpaq',
).link(book, linear_algebra)

add_pdf(
  name="Mathematical Methods For Physics",
  filename='mathematical-methods-for-physics.zpaq',
).link(book, math, physics)

add_pdf(
  name="Mathematical Physics",
  filename='mathematical-physics.zpaq',
).link(book, math, physics)

add_pdf(
  name="Mathematics For Computer Graphics And Game Programming",
  filename='mathematics-for-computer-graphics-and-game-programming.zpaq',
).link(book, math, graphics, gamedev)

add_pdf(
  name="Microsoft Excel Functions And Formulas With Excel2019 And Office365",
  filename='microsoft-excel-functions-and-formulas-with-excel2019-and-office365.zpaq',
).link(book, math, excel)

add_pdf(
  name="Multivariable And Vector Calculus",
  filename='multivariable-and-vector-calculus.zpaq',
).link(book, math)

add_pdf(
  name="Numerical Methods In Engineering And Science",
  filename='numerical-methods-in-engineering-and-science.zpaq',
).link(book, math)

add_pdf(
  name="Optimization Using Linear Programming",
  filename='optimization-using-linear-programming.zpaq',
).link(book, math)

add_pdf(
  name="Research Methods For Information Systems",
  filename='research-methods-for-information-systems.zpaq',
).link(book, math)

add_pdf(
  name="RF Module",
  filename='rf-module.zpaq',
).link(book, math)

add_pdf(
  name="Special Theory Of Relativity",
  filename='special-theory-of-relativity.zpaq',
).link(book, math, physics)

add_pdf(
  name="Structural Steel Design",
  filename='structural-steel-design.zpaq',
).link(book, math)

add_pdf(
  name="Android 9 Development Cookbook",
  filename='android-9-development-cookbook.zpaq',
).link(book, android)

add_pdf(
  name="Android Programming For Beginners",
  filename='android-programming-for-beginners.zpaq',
).link(book, android, java)

add_pdf(
  name="Android Programming With Kotlin For Beginners",
  filename='android-programming-with-kotlin-for-beginners.zpaq',
).link(book, android, kotlin)

add_pdf(
  name="Flutter For Beginners",
  filename='flutter-for-beginners.zpaq',
).link(book, flutter)

add_pdf(
  name="Hands On Android UI Development",
  filename='hands-on-android-ui-development.zpaq',
).link(book, android)

add_pdf(
  name="Hands On Full Stack Development With Swift",
  filename='hands-on-full-stack-development-with-swift.zpaq',
).link(book, swift, frontend, backend)

add_pdf(
  name="Hands On Serverside Web Development With Swift",
  filename='hands-on-serverside-web-development-with-swift.zpaq',
).link(book, swift, backend)

add_pdf(
  name="Ionic Cookbook",
  filename='ionic-cookbook.zpaq',
).link(book, ionic)

add_pdf(
  name="iOS 13 Programming For Beginners",
  filename='ios-13-programming-for-beginners.zpaq',
).link(book, ios)

add_pdf(
  name="Learn Swift By Building Applications",
  filename='learn-swift-by-building-applications.zpaq',
).link(book, swift)

add_pdf(
  name="Mastering Swift 5",
  filename='mastering-swift-5.zpaq',
).link(book, swift)

add_pdf(
  name="Mastering Xamarin UI Development",
  filename='mastering-xamarin-ui-development.zpaq',
).link(book, xamarin)

add_pdf(
  name="React Native Blueprints",
  filename='react-native-blueprints.zpaq',
).link(book, react_native)

add_pdf(
  name="React Native Cookbook",
  filename='react-native-cookbook.zpaq',
).link(book, react_native)

add_pdf(
  name="Swift Protocol Oriented Programming",
  filename='swift-protocol-oriented-programming.zpaq',
).link(book, swift)

add_pdf(
  name="Test Driven iOS Development With Swift 4",
  filename='test-driven-ios-development-with-swift-4.zpaq',
).link(book, ios, swift, tdd)

add_pdf(
  name="Xamarin Forms Projects",
  filename='xamarin-forms-projects.zpaq',
).link(book, xamarin)

add_url(
    name='Visual Studio Code',
    url='https://code.visualstudio.com/',
).link(software, free, editor)

add_url(
    name='Visual Studio',
    url='https://visualstudio.microsoft.com/',
).link(software, free, ide)

add_url(
    name='Emacs',
    url='https://www.gnu.org/software/emacs/',
).link(software, free, editor)

add_url(
    name="Ralf Brown's Interrupt List",
    url="http://www.ctyme.com/rbrown.htm",
).link(reference, assembly)

add_url(
    name="32bit DOS Development with Open Watcom",
    url="http://tuttlem.github.io/2015/10/04/32bit-dos-development-with-open-watcom.html",
).link(cpp, software, free)

add_url(
    name="Allegro",
    url="http://liballeg.org/"
).link(cpp, gamedev, library, free)

add_url(
    name="The Last Thing D Needs",
    url="https://www.youtube.com/watch?v=KAWA1DuvCnQ"
).link(cpp, video)

add_url(
    name="Godbolt Compiler Explorer",
    url="https://godbolt.org/",
    description="Compiler Explorer: Website that allows to compile code using a large collection of C++ compilers"
).link(cpp)

add_url(
    name="Unreal Engine",
    url="https://www.unrealengine.com/"
).link(cpp, framework, gamedev, free)

docker = add_url(
    name="Docker",
    url="https://www.docker.com/",
).link(virtualization, software, free)

add_url(
    name="Vagrant",
    url="https://www.vagrantup.com/",
).link(virtualization, software, free)

add_url(
    name="Dive Into Docker",
    url="https://diveintodocker.com/",
).link(docker, tutorial)

add_url(
    name="Docker Hub",
    url="https://hub.docker.com/",
).link(docker, tutorial)

add_url(
    name="NPM",
    url="https://www.npmjs.com/",
).link(javascript)

add_url(
    name="NodeJS",
    url="https://nodejs.org/",
).link(javascript, backend, software, free)

add_url(
    name="Impact Game Engine",
    url="https://impactjs.com/",
).link(javascript, gamedev, library)

add_url(
    name="PixiJS Game Engine",
    url="http://www.pixijs.com/",
).link(javascript, gamedev, library)

add_url(
    name="p5.js",
    url="https://p5js.org/",
).link(javascript, graphics, library)

add_url(
    name="Redux",
    url="https://redux.js.org/",
).link(javascript, library)

add_url(
    name="Webpack",
    url="https://webpack.js.org/",
).link(javascript)

add_url(
    name="Express",
    url="https://expressjs.com/",
).link(javascript, backend, library)

sinatra = add_url(
    name="Sinatra",
    url="http://sinatrarb.com/",
).link(ruby, backend, library, webdev)

add_url(
    name="Sinatra - The Book",
    url="https://sinatra-org-book.herokuapp.com/",
).link(sinatra)

sinatra = add_url(
    name="Ruby on Rails",
    url="https://rubyonrails.org/",
).link(ruby, backend, library, webdev)

add_pdf(
    name='Linear Algebra Done Right',
    filename='linear-algebra-done-right.zpaq'
).link(book, linear_algebra)

add_pdf(
    name='Abstract Algebra',
    filename='abstract-algebra.zpaq'
).link(book, algebra)

add_pdf(
    name='Topology (book)',
    filename='topology.zpaq'
).link(book, topology)

add_pdf(
    name='Theory of Numbers',
    filename='theory-of-numbers.zpaq'
).link(book, topology)
