TOKEN = "OTgwODYyNzgyNjgzNjMxNjU3.GgDAJU.-v4R70kTF0czfr8T15SAIcpuWjm8EIr3vVYyWY"

help_str = """
**Пользовательские команды**
`/russian-roulette` - сыграть в русскую рулетку.
`/fox` - рандомная картинка лисы с фактом о ней.
`/avatar [пинг]` - посмотреть аватар.
`/user [пинг]` - информация о пользователе.
`/save-reddit [url]` - сохранить видео или гиф с реддита.

**РП команды**
`/hug [пинг]` - обнять.
`/hugall` - обнять всех.
`/kiss [пинг]` - поцеловать.
`/pat [пинг]` - погладить.
`/eat [пинг]` - съесть.
`/catch [пинг]` - украсть.
`/kill [пинг]` - убить.
`/revive [пинг]` - воскресить.

**Мод. команды**
`/add-moderator-role [пинг]` - добавить модераторcкую роль.
`/remove-moderator-role [пинг]` - убрать модераторcкую роль.
`/set-death-role [пинг роли]` - установить роль для `!russian-roulette`.
`/set-suggestion-channel [пинг канала]` - установить канал для предложений.
"""

RP = {
    "hug": {
        "text": ['обхватил руками', 'приобнял', 'обнял', 'прижал к груди', 'прижал к сердцу', 'стиснул в объятиях'],
        "image": ['https://i.imgur.com/r9aU2xv.gif?noredirect', 'https://c.tenor.com/AO-1yttBeH8AAAAC/anime-hug.gif', 'https://media0.giphy.com/media/kAxLNi5oOzJq18GDGX/giphy.gif?cid=790b76', 'https://c.tenor.com/nhptHx9eZhYAAAAC/sloth-hug.gif', 'https://media.discordapp.net/attachments/881893798270083072/962030707000115230/sakura-quest-anime.gif', 'https://media.discordapp.net/attachments/881893798270083072/962030707314675782/anime-run.gif', 'https://media.discordapp.net/attachments/881893798270083072/962030707989938226/happy-hug.gif',  'https://cdn.discordapp.com/attachments/881893798270083072/962030708560384060/horimiya-hug-anime.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962030709051113472/hug.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962030709566996560/hug-anime.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962030709898375249/hug-anime-hug.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962030710485581885/hug-k-on.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962030711039213618/loli-dragon.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962030711399915600/rena-ryuuguu-satoko-hojo.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962030734380523550/anime-loli.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962030735244558476/anime-cuddles.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962030735508766720/anime-hug.gif', 'https://i.gifer.com/3OJ5R.gif', 'https://i.imgur.com/m5aSzlq.gif'],
        "emote": ["https://media.discordapp.net/attachments/881893798270083072/961998361626562570/876534780735389696_1.png", "https://media.discordapp.net/attachments/748481686811049986/986971358741266513/975730303865876491.png?width=618&height=556"],
        "self use text": 'некого обнять!',
        "self use image": ['https://media.giphy.com/media/TRgyI2f0hRHBS/giphy.gif', 'https://media.giphy.com/media/oAW9QPkQwJqJq/giphy.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962016307992203354/kanna-kanna-dragon.gif', 'https://media.discordapp.net/attachments/881893798270083072/962031064858107935/hestia-anime.gif', 'https://media.discordapp.net/attachments/881893798270083072/962031065160101909/kanna-kanna-dragon.gif'],
        "self use emote": "https://media.discordapp.net/attachments/881893798270083072/962015569647923210/845249592353882122.png"
    },
    "hugall": {
        "text": ['крепко всех обнял', 'позвал всех на обнимашки', 'всех обнял', 'прижал к всех разом', 'стиснул в объятиях весь сервер'],
        "image": ['https://cdn.discordapp.com/attachments/881893798270083072/962029675859812413/animes-anime.gif'],
        "emote": ["https://media.discordapp.net/attachments/881893798270083072/926810516318478366/876534780735389696.png", "https://images-ext-2.discordapp.net/external/7muLfHnzUmLAyrDuIGHEYSnCNIuRUktegSCV3ymygkg/https/cdn.discordapp.com/stickers/975730303865876491.png?width=618&height=556"],
    },
    "kiss": {
        "text": ['поцеловал с любовью', 'нежно поцеловал', 'подарил поцелуй'],
        "image": ['https://data.whicdn.com/images/190323288/original.gif', 'https://cdn.discordapp.com/attachments/915976584912060516/915976768870031380/aniyuki-anime-gif-kiss-35.gif', 'https://c.tenor.com/TnjL6WcdkkwAAAAd/anime-kiss.gif', 'https://media.discordapp.net/attachments/852259897340854326/883374811273904208/Kiss1.gif', 'https://media.discordapp.net/attachments/852259897340854326/883374819138211860/Kiss.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962027039211266088/kiss-me-.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962027040096268418/anime-couple.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962027040830275665/anime-kiss-love.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962027043015495810/cute-kawai.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962027043535618138/kiss.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962027043988582480/kiss-anime.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962027045171363870/kiss-anime13.gif'],
        "emote": "https://images-ext-1.discordapp.net/external/ILXtp3EQ5OvzoZNb1tf_VnbjwkrjODpBkPX70LYfEPw/https/media.discordapp.net/attachments/881893798270083072/926811529674891274/868449077241733160.png",
        "self use text": ['поцеловал своё отражение!','нежно поцеловал своё отражение!','подарил поцелуй своему отражение!'],
        "self use image": ['https://c.tenor.com/RUBvK3Ln2sMAAAAC/sarahmcfadyen-lewis-capaldi.gif', 'https://c.tenor.com/0-ZcXybzvIgAAAAC/edoardo-esposito-valerio-mazzei.gif', 'https://c.tenor.com/RYWDecZSEH0AAAAd/donny-most-self-hug.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/924609423643639868/23By.gif'],
        "self use emote": "https://media.discordapp.net/attachments/881893798270083072/962015966923984957/876793687970029568.png"
    },
    "eat": {
        "text": ['съел', 'пообедал', 'проглотил', 'с голоду съел'],
        "image": ['https://cdn.discordapp.com/attachments/881893798270083072/962366726710894662/breakfast-future-stan-marsh.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962366727100973137/eating-fast-panda-bear.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962366728220864512/eat-restaurant.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962366728728379422/mukbang-food.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962366729399439430/out-self-eat.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962366730028589137/patrick-star-funny-gifs.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962366730414489650/tkthao219-peach.gif'],
        "emote": "https://images-ext-2.discordapp.net/external/p3RoToHd1EpuoB7DsU2KkJn3q2-uvc08lLl71PRDUDo/https/media.discordapp.net/attachments/920619402016223233/938469319690559530/844585061549342730.png",
        "self use text": ['ест себя', 'сосёт свой палец', 'съел себя с голода'],
        "self use image": ['https://cdn.discordapp.com/attachments/881893798270083072/962366726228545626/weird-eating.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962369076246769724/giphy.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962369076515176518/----813707.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962369076838154291/dog-chasing-tail-5.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962369077496664064/dog-chasing-tail-7.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962369078125817986/dog-chasing-tail-24.gif'],
        "self use emote": "https://images-ext-1.discordapp.net/external/cxAlyuZaQz7jNdzT3-fexuLzCmY5N4VufYXPs6yG1lE/https/media.discordapp.net/attachments/920619402016223233/938469257308676106/852519210315022406.png"
    },
    "catch": {
        "text": ['украл', 'стырил средь бела дня'],
        "image": ['https://media4.giphy.com/media/tBb19fjQsnXRgMT3kZi/200.gif', 'https://media4.giphy.com/media/VHlKSFRTQ7nn81fkv4/200.gif', 'https://c.tenor.com/AlrUVwjmtDQAAAAC/yikes-running.gif', 'https://c.tenor.com/wOCMhN4bqokAAAAC/raccoon-steal.gif', 							'https://c.tenor.com/irsckaQsr2QAAAAC/thief-stealing.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962029456044736532/thief-car-thief.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962029457101684806/pickpocket-mr-wolf.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962029458196414535/raccoon-binatang.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962029458762657822/the-outpost-the-outpost-series.gif'],
        "emote": "https://media.discordapp.net/attachments/881893798270083072/926812972704227378/844585061549342730.png",
        "fail text": ['был пойман', "не смог стырить $user", 'был пойман с поличным'],
        "fail image": ['https://media4.giphy.com/media/tBb19fjQsnXRgMT3kZi/200.gif', 'https://media4.giphy.com/media/VHlKSFRTQ7nn81fkv4/200.gif', 'https://c.tenor.com/AlrUVwjmtDQAAAAC/yikes-running.gif', 'https://c.tenor.com/wOCMhN4bqokAAAAC/raccoon-steal.gif', 							'https://c.tenor.com/irsckaQsr2QAAAAC/thief-stealing.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962029410586869760/station19-andy-herrera.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962029411186642984/dance-draingangrunningaway.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962029411618664539/oh-shit-no.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962029412033912882/running-away-running.gif'],
        "fail emote": "https://media.discordapp.net/attachments/881893798270083072/926812972704227378/844585061549342730.png"
    },
    "pat": {
        "text": ['погладил', 'аккуратно погладил', 'похлопал по головушке', 'нежно погладил', 'с трепетом погладил', 'заботливо погладил, приласкал'],
        "image": ['https://cdn.discordapp.com/attachments/881893798270083072/962026572641079367/anime-senko-san.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026573085700106/dragon-maid-kobayashi.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026573622562857/k-on-anime.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026574054555718/mai-headpats.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026574364938300/123123.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026574935371776/anime-anime-girl.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026575417724928/anime-head-pat.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026576034275378/anime-head-pat1.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026576831205386/anime-pat.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026629209677885/pat-thats-okay.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026629507453019/pat-anime.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026629792694342/pat-head-pat.gif'],
        "emote": "https://images-ext-2.discordapp.net/external/hcDvjiVDQy0jqzTLO5848-kL6zNIeT56-4Qx8TeopIw/https/media.discordapp.net/attachments/881893798270083072/926811307552956466/919564492780765194.gif",
    },
    "kill": {
        "text": ['хладнокровно зарезал', 'сбросил с моста', 'задушил', 'застрелил', 'жестоко расчленил'],
        "image": ['https://i.pinimg.com/originals/79/c7/5c/79c75cccdf1dbb3b1fa403d607415059.gif', 'https://i.imgur.com/WNoJHps.gif', 'https://c.tenor.com/Zi1l60KaBGMAAAAC/among-us-kill.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026945481179136/mikey-tokyo.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026945887998032/a-channel-tooru.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026946294857838/akame-ga-kill-anime.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026946697515019/anime.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026947364388894/iron-golem-dream-dies.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026948094205962/kill-satanichia.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026948568174652/kill-smack.gif'],
        "emote": ['https://media.discordapp.net/attachments/881893798270083072/926813815297941577/844585061579751424.png', 'https://media.discordapp.net/attachments/881893798270083072/926814178029740032/1gun2.png', 'https://media.discordapp.net/attachments/881893798270083072/926814373282971688/a0bddce95287aa5a.png', 'https://media.discordapp.net/attachments/881893798270083072/926814487305130005/kill.png', 'https://media.discordapp.net/attachments/881893798270083072/926810961011167262/Alice_bonknew.png'],
        "self use text": ['не попал и убил себя', 'нечайно убил себя', 'не рассчитал и попал по себе'],
        "self use image": ['https://c.tenor.com/7TVZNUdJYQ0AAAAC/gun-shoot-me.gif', 'https://c.tenor.com/1JidhwQcI2YAAAAC/kill-myself.gif', 'https://c.tenor.com/SPl5QtWURCgAAAAC/spongebob-stabbing-himself-minul.gif', 'https://c.tenor.com/C1QVHrjYIrgAAAAd/slowdeath-killmenow.gif', 'https://c.tenor.com/_zbXkVfNRW0AAAAC/king-of-the-hill-hank.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026858902339634/you-died-ryan.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026859514724453/falling-you-died.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026860005437490/minecraft-die.gif', 'https://cdn.discordapp.com/attachments/881893798270083072/962026860307435570/minecraft-sword-die-lukiecas.gif'],
        "self use emote": "https://media.discordapp.net/attachments/881893798270083072/926814687658647572/881949007100915712.png"
    },
    "revive": {
        "text": ["воскрес", "был реанимирован", "вернулся в мир живых", "ожил", "вернулся с того света", "вернулся к жизни", "пробудился от вечного сна"],
        "image": ["https://cdn.discordapp.com/attachments/876388450331410472/919168850136821761/mercy-overwatchRevive.gif", "https://media.discordapp.net/attachments/880520858249072681/882226624001630238/overwatch-mercy.gif"],
        "emote": "https://media.discordapp.net/attachments/881893798270083072/926813271456096256/868449273166037022.png"
    }
}