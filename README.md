# MOONDROP — Listening collection

Готовая локальная некоммерческая витрина на Next.js App Router, TypeScript, Tailwind CSS, GSAP / ScrollTrigger, Lenis и Radix Dialog.

```sh
npm install
npm run dev
```

Адрес: http://localhost:3000

Production на Vercel: https://moondrop-listening-collection.vercel.app

Папка связана с проектом `moondrop-listening-collection`. Для публикации обновлений:

```sh
npx vercel deploy --prod --verify
```

Исследования, скриншоты, локальные переменные окружения и служебные файлы исключены через `.vercelignore`. Деплой выполняется через CLI; автоматическая публикация из Git не настроена.

```sh
npm run typecheck
npm run lint
npm run build
npm start
```

Основная страница — серверный компонент. Клиентские острова отвечают за движение, доступные диалоги и синтезированный эмбиент Web Audio. Изображения и шрифты хранятся в public/assets; внешних запросов для отображения нет. Ссылки открывают официальные страницы.

Дизайн: DESIGN.md. Источники и права: SOURCES.md и /sources.html. Скриншоты: screenshots/. Воспроизводимая браузерная проверка: scripts/verify_site.py (Python Playwright и установленный Chrome).

Это не магазин и не официальный сайт MOONDROP. Нет оплаты, аналитики, аккаунтов и серверной базы. Аудио является синтезированным фоном, а не записью наушников. Максимальное разрешение отдельных официальных товарных рендеров — 500×500; более крупная сцена COSMO использует отдельное фото 1000×923.
