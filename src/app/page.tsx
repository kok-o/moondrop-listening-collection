import Image from "next/image";
import { products } from "@/lib/products";
import { Arrow } from "@/components/Arrow";
import { ProductDetails } from "@/components/ProductDetails";
import { MotionDirector } from "@/components/MotionDirector";
import { SoundControl } from "@/components/SoundControl";

function SoundWave() {
  const paths = Array.from({ length: 19 }, (_, i) => {
    const points = Array.from({ length: 121 }, (_, j) => {
      const x = j * 12;
      const envelope = Math.exp(-Math.pow((j - 61) / 34, 2));
      const y =
        260 +
        Math.sin(j * 0.095 + i * 0.15) *
          Math.cos(j * 0.028 + i * 0.03) *
          envelope *
          (90 + i * 5);
      return `${j === 0 ? "M" : "L"}${x.toFixed(1)},${y.toFixed(1)}`;
    }).join(" ");
    return (
      <path
        key={i}
        d={points}
        stroke={i % 3 === 0 ? "#d9b0bc" : "#727984"}
        strokeOpacity={i % 3 === 0 ? ".7" : ".36"}
        strokeWidth=".85"
      />
    );
  });
  return (
    <svg
      className="sound-wave"
      viewBox="0 0 1440 520"
      fill="none"
      aria-hidden="true"
    >
      {paths}
    </svg>
  );
}

export default function Home() {
  return (
    <>
      <a href="#collection" className="skip-link">
        Перейти к коллекции
      </a>
      <header className="site-header">
        <a className="brand" href="#top" aria-label="MOONDROP — в начало">
          <Image src="/assets/logo.svg" alt="" width={36} height={38} preload />
          <span>MOONDROP</span>
        </a>
        <nav aria-label="Основная навигация">
          <a href="#collection">Коллекция</a>
          <a href="#sound">Философия звука</a>
          <a href="#compare">
            Найти свои <Arrow diagonal />
          </a>
        </nav>
        <span className="header-edition">
          Независимая редакция <span>2026</span>
        </span>
      </header>
      <main id="top">
        <section className="hero-stage" aria-labelledby="hero-heading">
          <div className="hero-scene">
            <div className="hero-kicker">
              <span className="small-cross">✳</span>
              <span>Там, где точность становится чувством</span>
              <span className="edition-tag">Art meets acoustics</span>
            </div>
            <div className="hero-word" aria-hidden="true">
              MOONDROP<span>®</span>
            </div>
            <div className="hero-orbit" aria-hidden="true" />
            <div className="hero-copy">
              <div className="vertical-mark" aria-hidden="true">
                水月雨
              </div>
              <p className="micro hero-intro">Искусство слышать</p>
              <h1 id="hero-heading">
                Между звуком
                <br />и чувством.
              </h1>
              <p className="hero-description">
                Точная инженерия. Свободное воображение.
                <br className="desktop-break" /> Твоя музыка — чуть ближе к
                тебе.
              </p>
              <a className="button button-dark" href="#collection">
                Открыть коллекцию <Arrow />
              </a>
            </div>
            <div className="yuki-art">
              <Image
                src="/assets/yuki-cosmo-ink.webp"
                alt="Mitsuki Yuki слушает музыку в COSMO. Официальная иллюстрация MOONDROP в красных и голубых контурах."
                fill
                preload
                sizes="(max-width:600px) 110vw, (max-width:900px) 80vw, 61vw"
              />
            </div>
            <div className="art-caption">
              <span className="caption-line" />
              <span>
                Mitsuki Yuki
                <br />
                <small>Наш проводник в мир звука</small>
              </span>
            </div>
            <div className="hero-product">
              <Image
                src="/assets/cosmo-render.webp"
                alt="MOONDROP COSMO — серебристые планарные наушники"
                fill
                preload
                sizes="(max-width:600px) 210px, (max-width:900px) 300px, 410px"
              />
              <span className="product-coordinate">COSMO / 100 mm planar</span>
            </div>
            <div className="handoff-copy" aria-hidden="true">
              <span className="micro">За каждым чувством — точность.</span>
              <h2>
                Меньше шума.
                <br />
                Больше музыки.
              </h2>
              <p>
                От эскиза к инженерии.
                <br />
                От первой ноты — к целой вселенной.
              </p>
              <span className="text-link">
                Найди свой звук ниже <Arrow />
              </span>
            </div>
            <div className="hero-bottom">
              <a href="#collection" className="scroll-cue">
                <span>↓</span> Листай. Прислушивайся.
              </a>
              <p>
                Воображение без границ.
                <br />
                Звук без случайностей.
              </p>
              <span className="hero-index">
                MOONDROP <span>Listening collection</span>
              </span>
            </div>
          </div>
        </section>

        <section
          id="collection"
          className="collection section-pad"
          aria-labelledby="collection-title"
        >
          <div className="section-heading">
            <div>
              <p className="micro section-label">
                <span className="dot" /> Подобрано для тебя
              </p>
              <h2 id="collection-title">
                Три характера.
                <br />
                Твой резонанс.
              </h2>
            </div>
            <p>
              У каждого свой способ слушать.
              <br />
              Найди тот, который звучит в унисон с тобой.
            </p>
          </div>
          <div className="collection-grid">
            <article className="product-card travel-card">
              <div className="card-topline">
                <span>В твоём ритме</span>
                <span>Беспроводные</span>
              </div>
              <div className="product-image-link">
                <Image
                  src={products[0].image}
                  alt={products[0].imageAlt}
                  fill
                  sizes="(max-width:600px) 90vw, 45vw"
                  className="card-product"
                />
              </div>
              <div className="product-card-copy">
                <p className="micro">{products[0].category}</p>
                <h3>SPACE TRAVEL</h3>
                <p className="card-description">{products[0].tagline}</p>
                <div className="card-specs">
                  <span>Bluetooth 5.3</span>
                  <span>4 ч + 12 ч с кейсом</span>
                </div>
                <ProductDetails product={products[0]} />
              </div>
              <span className="card-ghost" aria-hidden="true">
                TRAVEL
              </span>
            </article>
            <article className="product-card dusk-card">
              <div className="card-topline">
                <span>MOONDROP × Crinacle</span>
                <span>Гибридные IEM</span>
              </div>
              <div className="product-image-link">
                <Image
                  src={products[1].image}
                  alt={products[1].imageAlt}
                  fill
                  sizes="(max-width:600px) 90vw, 45vw"
                  className="card-product"
                />
              </div>
              <div className="product-card-copy">
                <p className="micro">{products[1].category}</p>
                <h3>DUSK</h3>
                <p className="card-description">{products[1].tagline}</p>
                <div className="card-specs">
                  <span>2DD + 2BA + 2 Planar</span>
                  <span>3,5 мм / USB-C</span>
                </div>
                <ProductDetails product={products[1]} />
              </div>
              <span className="card-ghost" aria-hidden="true">
                DUSK
              </span>
            </article>
          </div>
          <article className="cosmo-feature">
            <div className="cosmo-feature-visual">
              <Image
                src="/assets/cosmo-detail.webp"
                alt="Макросъёмка металлической решётки и амбушюр COSMO"
                fill
                sizes="(max-width:600px) 100vw, 53vw"
              />
              <span className="detail-annotation">
                Серебро снаружи. Вселенная внутри.
              </span>
            </div>
            <div className="cosmo-feature-copy">
              <p className="micro">Флагманские планарные наушники</p>
              <h3>COSMO</h3>
              <h4>
                Оставь место
                <br />
                для большего.
              </h4>
              <p>{products[2].description}</p>
              <div className="cosmo-facts">
                <div>
                  <strong>
                    100<span>мм</span>
                  </strong>
                  <span>Планарная диафрагма</span>
                </div>
                <div>
                  <strong>
                    15<span>Ω</span>
                  </strong>
                  <span>Импеданс при 1 кГц, ±15%</span>
                </div>
              </div>
              <ProductDetails product={products[2]} />
            </div>
          </article>
        </section>

        <section
          id="sound"
          className="sound-scene"
          aria-labelledby="sound-title"
        >
          <div className="sound-top">
            <span className="micro">
              <span className="dot" /> Чувствовать частоту
            </span>
            <span className="micro">水月雨 / MOONDROP</span>
          </div>
          <div className="sound-heading">
            <h2 id="sound-title">
              Всё начинается
              <br />с тишины.
            </h2>
            <p>
              А потом приходит звук.
              <br />И всё остальное перестаёт иметь значение.
            </p>
          </div>
          <SoundWave />
          <div className="sound-product">
            <Image
              src="/assets/cosmo-dark.webp"
              alt="COSMO в тёмной студии — свет очерчивает металлические чаши"
              fill
              sizes="(max-width:600px) 92vw, 500px"
            />
          </div>
          <div className="sound-bottom">
            <div className="sound-quote">
              <span aria-hidden="true">“</span>
              <p>
                Искусство и разум.
                <br />В одной частоте.
              </p>
            </div>
            <SoundControl />
          </div>
        </section>

        <section
          id="compare"
          className="comparison section-pad"
          aria-labelledby="compare-title"
        >
          <div className="section-heading">
            <div>
              <p className="micro section-label">
                <span className="dot" /> Самое личное решение
              </p>
              <h2 id="compare-title">
                Как звучит
                <br />
                твой мир?
              </h2>
            </div>
            <p>
              Не лучше. Не громче.
              <br />
              Ближе к тому, что любишь именно ты.
            </p>
          </div>
          <div className="compare-grid">
            {products.map((p, i) => (
              <article className="compare-model" key={p.id}>
                <div className="compare-image">
                  <Image
                    src={p.image}
                    alt=""
                    fill
                    sizes="(max-width:600px) 140px, 260px"
                  />
                </div>
                <div className="compare-content">
                  <p className="micro">
                    {i === 0
                      ? "В городе и в движении"
                      : i === 1
                        ? "Для внимательного прослушивания"
                        : "Для домашних музыкальных сессий"}
                  </p>
                  <h3>{p.name}</h3>
                  <dl>
                    <div>
                      <dt>Формат</dt>
                      <dd>
                        {i === 0
                          ? "Беспроводные"
                          : i === 1
                            ? "Внутриканальные"
                            : "Полноразмерные"}
                      </dd>
                    </div>
                    <div>
                      <dt>{i === 0 ? "Соединение" : "Драйвер"}</dt>
                      <dd>{p.feature}</dd>
                    </div>
                    <div>
                      <dt>{i === 0 ? "Автономность" : "Подключение"}</dt>
                      <dd>
                        {i === 0
                          ? "4 ч + 12 ч с кейсом"
                          : i === 1
                            ? "3,5 мм / USB-C"
                            : "Балансный 4,4 мм"}
                      </dd>
                    </div>
                  </dl>
                  <a
                    href={p.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="official-link"
                    aria-label={`${p.name} на официальном сайте`}
                  >
                    На сайт MOONDROP <Arrow diagonal />
                  </a>
                </div>
              </article>
            ))}
          </div>
        </section>
        <section className="closing-note">
          <span aria-hidden="true">水月雨</span>
          <p>
            Музыка ближе,
            <br />
            чем кажется.
          </p>
          <a
            href="#top"
            className="back-top"
            aria-label="Вернуться в начало страницы"
          >
            ↑
          </a>
        </section>
      </main>
      <footer className="site-footer">
        <div className="footer-top">
          <a href="#top" className="brand" aria-label="MOONDROP — в начало">
            <Image src="/assets/logo.svg" alt="" width={36} height={38} />
            <span>MOONDROP</span>
          </a>
          <p>
            Независимый некоммерческий fan concept.
            <br />
            Создан из любви к музыке и дизайну.
          </p>
          <a
            href="https://moondroplab.com/en/home"
            target="_blank"
            rel="noopener noreferrer"
          >
            Официальный MOONDROP <Arrow diagonal />
          </a>
        </div>
        <div className="footer-bottom">
          <span>© 2026 · Fan concept</span>
          <p>
            Продукты, логотип и иллюстрация Mitsuki Yuki © MOONDROP.
            <br className="mobile-break" />{" "}
            <a href="/sources.html">Материалы и источники</a>
          </p>
          <span>Слушай. Чувствуй.</span>
        </div>
      </footer>
      <MotionDirector />
    </>
  );
}
