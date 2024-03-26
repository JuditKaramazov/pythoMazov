# pythoMazov

<p align="center">
  <a href="https://pythomazov.tech">
    <img src="./assets/pythoFooter.png" width="170" alt="pythoMazov original logo.">
  </a>
</p>
<p align="center">
  <strong><span style="font-size: larger;">Or how to become a Snake Eater</span></strong>
</p>


<div align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python badge" title="Python" />
  <img src="https://img.shields.io/badge/reflex-black.svg?style=for-the-badge&logo=reflex" alt="Reflex badge" title="Reflex" />
  <img src="https://img.shields.io/badge/chakra-%234ED1C5.svg?style=for-the-badge&logo=chakraui&logoColor=white" alt="Chakra badge" title="ChakraUI" />
</div>

<p align="center">
  <a href="https:/github.com/JuditKaramazov">🐱 /JuditKaramazov</a>
</p>
<p align="center">
  <a href="https://karamazfolio.xyz/">📍 Portfolio</a>
</p>
<p align="center">
  <a href="https://karamablog.xyz">☕ Blog</a>
</p>
<p align="center">
  <a href="https://pythomazov.tech">🌐 App</a>
</p>

---

Table of Contents
-----------------

* [🔧 Getting Started](#-getting-started)
* [🚪 Introduction](#-introduction)
* [🧬 Structure](#-structure)
  * [🛢️ Supabase](#-supabase)
  * [🐳 Docker](#-docker)
  * [🚂 Railway](#-railway)
* [🔮 Features](#-features)
  * [🔗 Links](#-links)
  * [📝 Content](#-content)
  * [🪝 Original book](#-original-book)
* [🧪 Scripts](#-scripts)
* [💄 Style](#-style)
* [🥳 Immense thanks to them awesome Sponsors](#-immense-thanks-to-them-awesome-sponsors)
* [🏛 License & Copyright](#-license--copyright)

---

# 🔧 Getting Started

Are you tired of things being extremely complicated _all the time_? [Reflex](https://reflex.dev/) (formerly **Pynecone**) is here to make web development easier - _and_ it will also make your wishes come true, no matter how twisted they are! (_Maybe I'm exaggerating a bit here._) 

This beautiful and reflexive framework **unifies the frontend and backend**, allowing you to create both using purely... any guess? Python, of course! Although this pure-Python beauty is **easy to learn** (no other languages required, and no need for a huge amount of experience either), Reflex remains as flexible as traditional web frameworks; it couldn't be smoother to get started, but it's still **powerful enough for advanced use cases**. A small data science app? A large, multi-page website? **Fear not**, fellow traveler. 

Does this introduction sound _noice_ enough? If that is the case, and if by any chance you'd want to get started with Reflex and its beginner-friendly wonders, allow me to guide you along the way.

First, clone this repository:

```bash
$ git clone https://github.com/JuditKaramazov/pythoMazov.git
```

Take into account that you'll need an `.env` file containing some essential keys, such as:

```
SUPABASE_KEY="..."
SUPABASE_URL="..."
```

Independently of further requirements related to my specific backend needs, you'll first have to [install and create a virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) using `pip`, just like you'll see below:

- **Mac/Linux**: `python3 -m pip install virtualenv`
- **Windows**: `py -m pip install --user virtualenv`

And:

`python3 -m venv .venv`

As for the virtual environment activation, similar to what you'll find in the [local_build.sh file](local_build.sh), you may want to follow these guidelines:

```
source .venv/bin/activate
python -m pip install -r requirements.txt
reflex init
```

This way, you will successfully **activate the virtual environment**, **install the necessary dependencies** (you'll find them in the [requirements.txt file](requirements.txt)), and **initialize the project**. 

Finally, in order to execute this little app, simply type:

`reflex run`

`"What comes after that, Judit?"` Huh, well... You simply have fun playing around! Remember, though: one of Reflex's standout features is its “batteries included” approach, which encompasses **everything you need to build a web application** — from the frontend to the backend — all within the confines of the Reflex framework. This way, we'll access [http://localhost:3000](http://localhost:3000) for the frontend, and [http://localhost:8000](http://localhost:8000) for the backend!

---

# 🚪 Introduction

Lately, I've been thinking a lot about the concept of "caves" and how we made them interact and coexist with technology, as if they were meant to be necessarily correlated, even intertwined, independently of our real wishes and mental preconceptions of what a cave _truly is_ (`Wait, wait... Were you still alive, Judit?` Eh, I'm trying to get philosophical here - and _of course_ I was. Am. Can't use any future formulas, though). 

As explained by [Bookwargames](https://videogameacademia.org/2022/08/01/jacobs-ladder-video-essay-review-jacob-geller/):

> Going up is the natural counterpart to going down. And we have to do both. Ascending and descending. To the mountaintop or to the riverbank. Upon the hills and through the valley. Out of the cave and into the light.

If we were to guess, what's this specific point of the Rabbit Hole? Where would you locate your exact position? Closer to the the light, or at the very bottom of a never-ending tunnel that keeps going deeper, and deeper? Are we metaphorically occupying the position of [Floyd Collins](https://en.wikipedia.org/wiki/Floyd_Collins), an experienced cave explorer from Kentucky who ended up trapped in a narrow passage of a cave _he owned_? Aren't the eternal passages of our dearly beloved interconnectivity somehow similar?

After some hours absorbed in thought due to the immensity of the above-mentioned idea, I stopped verbally phrasing these representations in my head and proceeded to go back to some video games that had the sensitivity to draw this "fear of the depths" and make it into a sensorial, corrosive experience. Can you remember _that_ specific moment of [INSIDE](https://store.steampowered.com/app/304430/INSIDE/), thrown into an abyss of water and... nothingness? That's how the corridors of the internet feel to me, somehow - and there is no way we can simplify the interconnections and possibilities it offers without finding a sturdy wall in front of us, just like it used to happen when our character wasn't following the right direction.

![Alt text](/assets/screenshots/pythoMazov-01.png)

That's probably a "good" way to describe what my "pseudo-book", [Rising Up: Insights from a Junior to Future Seniors](https://github.com/JuditKaramazov/InsightsFromJuniorToFutureSeniors), appeared to be when I first conceived it: a chaotic, claustrophobic amalgamation of files redirecting to new files that would _undoubtedly redirect you_ to the resource you _actually_ wanted to investigate. "Exploration time", some would say. However, we can still give interconnectivity the right direction, and this thought made me realize that, if I wanted my content to be as accessible as possible for users other than `them sexy GitHub naturals`, I would have to find a better approach covering different needs, preferences, and profiles.

To many people around me (I might include myself here as well), this year has been a lot like Sand Cave was for Floyd Collins. In your opinion, how far from the surface are we now? It seems that we'll have to find a way out together before we get to perish inside our own cave, which in my case lives under the [pythoMazov](https://pythomazov.tech) name.

---

# 🧬 Structure

I would genuinely love to start by saying that the entire structure of this project represents a `cave`. Although that affirmation is _partially true_, we will first define the **integration of our (still simple by now) database**, our **Dockerfile**, and the way **Railway uses it**. Remember that you'll find the final version of the website [in the following link](https://pythomazov.tech)!

Now, let's have a look at our **main flow**:

| Step                                                  | Description                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **GitHub Integration**                               | 🔄 After the initial development phase (where the project is built and tested locally), the code is pushed to GitHub, which serves as a central repository for version control.                                                                                                                                                                                                           |
| **GitHub Action for Static Resource Generation**      | 🛠️ [GitHub Actions](https://docs.github.com/en/actions) are configured to automatically trigger the generation of static resources for the project. These resources (HTML, CSS, and JavaScript files) are essential components of the web application and are linked to the project's repository.                                                                                                                          |
| **Deployment to Vercel**                             | 🚀 Once the resources have been generated, a trigger initiates the deployment process on [Vercel](https://vercel.com/). Vercel hosts the front end of the application, ensuring it is accessible to users over the internet. This step makes the deployment and hosting of the project's front end possible.                                                                                      |
| **Deployment to Railway with Dockerfile**            | 🚂 After Vercel's deployment, a trigger is activated in [Railway](https://railway.app/), a platform for hosting and managing backend services. Railway utilizes the project's [Dockerfile](./Dockerfile) to generate a container image containing the necessary dependencies and configurations for the backend. This image is then used to execute the process that exposes the API to clients. |

Now, more graphically yet quite simplified:

![Alt text](/assets/screenshots/pythoMazov-02.png)

> [!NOTE]
> To ensure secure communication between the frontend and the backend, [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) policies have been implemented. Remember that CORS restricts access to resources based on their origin, preventing unauthorized requests from accessing sensitive data or functionality.

## 🛢️ Supabase

What has [Supabase](https://supabase.com/) to do with our flow? In this case, its usage responds to _obscure wishes of mine_ and future implementations that I would want to explore further in the future, but at a fundamental level, the integration of a database becomes inevitable in the lifecycle of many projects. As Supabase simplifies this process quite a lot by providing a great API layer over PostgreSQL (with all the robust features of such a mature and powerful relational database system imply), and even though I didn't even consider this option at first, it is unquestionable that, as projects evolve, Supabase feels like the perfect support for data storage and management needs.

You don't want to know about the kind of skeletons that I'm hiding in my data-closet, though. Not yet, at least.

> [!TIP]
> For a deeper dive on Supabase, and just in case you happen to be an [🧑‍🚀 Astro 🚀](https://astro.build/) lover just like me, you can learn how to initialize Supabase in Astro [by following this dedicated guide](https://docs.astro.build/en/guides/backend/supabase/). 

## 🐳 Docker

In this case, our [Dockerfile](./Dockerfile) defines the steps necessary to create a Docker image for our backend service, which enables its packaging and deployment as a containerized application.

If you are not used to Docker, allow me to give you a brief explanation of some key concepts: one of the primary benefits of Docker is the **ability to package** our application along with its dependencies into a single, lightweight, portable, and self-contained unit called `container`. On the one hand, this ensures **consistency across different environments**, including development, testing, and production, as Docker ensures consistent behavior regardless of the underlying environment. On the other hand, Docker and its containers **eliminate the need to install and configure dependencies manually on each server or environment**. This way, we can easily deploy our application to any environment that supports Docker, streamlining the deployment process and reducing the presence of configuration errors.

Remember that, in order to build our Docker image, we will have to navigate to the directory containing the Dockerfile, and then execute the following command:

```bash
docker build -t beautiful-backend-image:latest .
```

In our case, `pythoMazov` replaced the `beautiful-backend-image` name (`docker build -t pythoMazov:latest .`), but that's completely up to you. 

![Alt text](/assets/screenshots/pythoMazov-03.png)

Once the image is built, you can run a container based on the previously-created image using:

```bash
docker run -d --name beautiful-backend-container beautiful-backend-image

```

> [!TIP]
> Since checking the available documentation is key in the development sector, refer to [Docker docs](https://docker-docs.uclv.cu/) in order to learn how to get started, follow some guides, and more!

## 🚂 Railway

What a blessing [Railway](https://docs.railway.app) is! Automatic builds, deployment rollbacks, multiple environments... although other platforms will allow you to achieve similar results (let's not forget that Railway.app, which happens to be a relatively new infrastructure, is inspired by [Heroku](https://www.heroku.com)), it's always interesting to see how different services bring their unique approach to cloud computing.

Whatever the case, here we are deploying our backend as a Docker container from Railway, which holds the personal API we created for the ocassion. As we'll briefly mention later on, we referenced the value of our `API_URL` in the [`remote_build.sh`](remote_build.sh) script, but what's necessary to highlight for now is that, compared to Heroku (where our apps simply shut down if they do not receive any input for around 30 minutes), **deployments on Railway run indefinitely**, and as it supports Docker files and Python... it seemed like a perfect excuse to give several tools a try!

> [!TIP]
> Do apps dream of electric sheep? If that's the question you had in mind before reaching this little reminder, feel free to check [the following article](https://blog.railway.app/p/launch-week-01-scale-to-zero), which dives a bit deeper into how exactly Railway handles your traffic when the container is not running. 

---

# 🔮 Features

Remember when I told you that the entirety of this double-project felt a bit like a `cave` to me? Soon, you'll clearly understand what I meant. Do not panic yet, though; the main features that I'll describe here are rather simple, but I considered it could be great to expose them openly just so that you can know what to expect.

Some unmentioned components are aimed at making navigation more accessible, like an integrated [sidebar menu](./pythomazov/components/navbar.py) or a [BackTop float button](./pythomazov/components/ant_components.py) allowing you to smoothly get back to the top of the web page without losing your fingerprints in the process. However, some other elements are worth mentioning instead - at least from a content perspective.

## 🔗 Links

Similarly to many portfolios and "link-in-bio" tools these days ([Linktree](https://linktr.ee/) was my biggest reference and inspiration), I decided to organize my website following the structure of a **landing page with associated links** that are mostly **unrelated to any social media**. Although there is the opportunity for you to contact or support me, I genuinely loved the concept of having a tool helping me share "everything I am" in a simple way, making my content **more discoverable**, **easier to manage**, and **more likely to convert**.

![Alt text](/assets/screenshots/pythoMazov-04.png)

I've never been particularly interested in showcasing my presence online; that's why I chose to omit the social layer of Linktree and focus on displaying, in an organized way, **multiple services and tools that I believe might be relevant for programming learners**.

## 📝 Content

Closely linked (_ha, ha..._) to the previous idea, the [`routes.py`](./pythomazov/routes.py) file defines what follows:

```python
from enum import Enum


class Route(Enum):
    INDEX = "/"
    COURSES = "/courses"
    CHEATSHEETS = "/cheatsheets"
    CHALLENGES = "/challenges"
```

I think it becomes way easier to understand the structure we followed in [pythoMazov](https://pythomazov.tech) thanks to these routes:

1. **Index, "/"**

  - The main page, containing links divided into **Starter Kit** (the main learning material offered on the website), **Useful resources** (a list of books, websites, and other utilities, like my personal setup), **Stay tuned** (reserved for my personal blog, where I write about technology, video games, and development), and a **Contact & Support section**. It is also possible to find the source for all the courses, cheat sheets, and other content you'll find in the previous links, as well as a dedicated place for our sponsor!

2. **"/courses"**

  - It can be accessed through the index ("Starter Kit"), and it offers both **my own courses and certificated ones**. At the moment, only **Python and Git/GitHub** are available, but I hope you'll find them clear, helpful, and accessible.

3. **"/cheatsheets"**

  - A hub for **my Python and Git cheat sheets**. First, I'll focus on finishing that specific content, but I'd gladly cover other languages if these two ones prove to be useful!

4. **"/challenges"**

  - Accessed through the index ("Learn by coding"), these links won't redirect you to my own material; instead, I gathered some of the most practical websites making learning challenging, engaging, and motivating. Codewars, Exercism, Codédex... no matter if you are into traditional challenges or gamified ones, this is the perfect place for you.


## 🪝 Original book

Except for the "Challenges" part, all the content listed above lives under a mono-repository (_even "pseudo-book", according to some_) that I myself created:

<p align="center">
  <img src="/assets/pythoLogo.png" alt="Original pythoMazov & 'Rising Up: Insights from a Junior to Future Seniors' logo." width=150 height=110>
  <br>
  <a href="https://github.com/JuditKaramazov/InsightsFromJuniorToFutureSeniors">Rising Up: Insights from a Junior to Future Seniors</a>
</p> 

Although I won't overexplain the motivations behind this specific work, the truth is that I made the active (_and mentally endangering_) decision of **creating a repository listing, explaining, and sharing resources that range from free online books to customized courses and cheat sheets**. Since I considered this kind of content might be relevant for those wishing to become part of this _beautiful sector of ours,_ I first wrote the entire content of that "book", and then **thought of an accessible alternative** to make the navigation intuitive and smooth.

![Alt text](/assets/screenshots/pythoMazov-05.png)
<p align="center">
  <i>This is where the website will redirect you to after choosing "Your IDE and you", located in "/courses"</i>
</p> 

Can you see now why I keep thinking of caves? It feels like a Rabbit Hole leading somewhere, and then somewhere else through the never-ending tunnels of interconnectivity; these two projects **wouldn't exist without the other**, as if they were some sort of indivisible twins. 

That's why navigating them feels like getting lost in a surprisingly-welcoming cave to me.

--- 

# 🧪 Scripts

In order to facilitate the process, there are two available scripts:

1. [`local_build.sh`](/local_build.sh)

  - It **activates a Python virtual environment**, **upgrades** the `pip` package, **installs Python dependencies** listed in the [`requirements.txt`](/requirements.txt) file, **removes the `public` directory** before exporting new frontend assets, **initializes Reflex**, **exports the frontend assets**, **extracts the contents of the `frontend.zip` file into the `public` directory**, **removes the `frontend.zip` file** after extraction and, finally, **deactivates the Python virtual environment**. It is used in **local development**.

  ```bash
  source .venv/bin/activate
  pip install --upgrade pip
  pip install -r requirements.txt
  rm -rf public
  reflex init
  reflex export --frontend-only
  unzip frontend.zip -d public
  rm -f frontend.zip
  deactivate
```

2. [`remote_build.sh`](/remote_build.sh)

  - Quite similar to the previous script, with the difference that, in this case, it **creates the remote build for production**. As you will see above, it incorporates our backend under the `API_URL` value.

  ```shell
  python -m venv .venv
  source .venv/bin/activate
  pip install --upgrade pip
  pip install -r requirements.txt
  rm -rf public
  reflex init
  API_URL=https://api.pythomazov.tech reflex export --frontend-only
  unzip frontend.zip -d public
  rm -f frontend.zip
  deactivate
  ```

---

# 💄 Style

Very cleverly, Reflex uses [tailwindcss](https://tailwindcss.com/) and [Chakra UI](https://chakra-ui.com/) for styling. As for the latest, it is a simple, modular, and accessible component library that gives you the building blocks you need to build your applications. "Less code, more speed" is an admittedly _noice_ moto, isn't it?

![Alt text](/assets/screenshots/pythoMazov-06.png)

> [!WARNING]
> Newer versions of Reflex do not use Chakra UI anymore; instead, they chose [Radix](https://www.radix-ui.com/) as their main fighter. It is as simple as substituting `rx.chakra.image()` by `rx.image()`, though!

As it won't surprise the ones who already know a couple of things about my repositories, I would want to gently thank [`@AuNedelec`](https://github.com/AuNedelec) for her support, amazing logos, and extreme patience whenever I decide to give her art apps a try.

Although these are indeed difficult times, I genuinely hope you'll eventually find [this website](https://pythomazov.tech), as well as the so-called ["pseudo-book"](https://github.com/JuditKaramazov/InsightsFromJuniorToFutureSeniors), a nice cave to get yourself healed. This project wouldn't exist without the inspiration you provided me with, after all.

---

# 🥳 Immense thanks to them awesome Sponsors

And this `cave` wouldn't exist without my amazing Sponsor,`@Entreprises LEMRHALI`, either. Funnily enough, the first time I showed you the logo you so warmly embraced, it only existed _here_, as part of [pythoMazov](https://pythomazov.tech). Although I sent it to you separately, I must admit I wasn't ready to receive such an incredily-great response - and _that_ fact made me extremely happy, as I added the notes, details, and "touches" that are so closely linked to you in my head.

We started several journeys together, such as the one represented by that logo. I just wish many other ones are yet to come (_especially now that Elden Ring is about to get new content..._). For all those moments, as well as for the future ones: `thank you` kindly.

<p align="center">
  <img src="./assets/lemrhali-entreprises.png" width="140" alt="Original Lemrhali Entreprises logo."
    style="filter: drop-shadow(0px 0px 10px rgba(0, 0, 0, .7));">
</p>

---

# 🏛 License & Copyright

God save our [MIT License](LICENSE.txt) and its infinite benevolence! That said, and only if you enjoyed the resources or the little apllication you found here, remember that you can make the Dinosaur of the Depths extremely happy if you...
<br />

---

<h1 align="center">
  <a href="https://karamazfolio.xyz/"><img src="https://raw.githubusercontent.com/JuditKaramazov/JuditKaramazfolio/a7b1825e33711948f51e53e249751761e1779f56/public/karamaBrand.png" width="100" height="100" alt="Original Karama logo asset.">
</h1>
<h2 align="center">
  <a href="https://www.buymeacoffee.com/JuditKaramazov" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 207px !important;" ></a>
</h2>
