import { useRouter } from 'next/router'
import type { DocsThemeConfig } from 'nextra-theme-docs'
import { useConfig } from 'nextra-theme-docs'

const logo = (
  <>
  <img src="/logo-dark.png" alt="Logo" height="40px" width="40px" />
  <span style={{ marginLeft: '.4em', fontWeight: 800 }}> Cogwheel Docs </span>
  </>
)

const config: DocsThemeConfig = {
  project: {
    link: 'https://github.com/Cogwheel-Validator'
  },
  docsRepositoryBase: 'https://github.com/Cogwheel-Validator/docs',
  useNextSeoProps() {
    const { asPath } = useRouter()
    if (asPath !== '/') {
      return {
        titleTemplate: '%s – Cogwheel Validator ⚙️'
      }
    }
    else {
      return {
        titleTemplate: 'Docs - Cogwheel Validator ⚙️'
      }
    }
  },
  editLink: {
    content: null
  },
  logo,
  darkMode: true,
  chat: {
    link: 'https://twitter.com/cogwheel_val',
    icon: (
      <svg width="24" height="24" viewBox="0 0 248 204">
        <path
          fill="currentColor"
          d="M221.95 51.29c.15 2.17.15 4.34.15 6.53 0 66.73-50.8 143.69-143.69 143.69v-.04c-27.44.04-54.31-7.82-77.41-22.64 3.99.48 8 .72 12.02.73 22.74.02 44.83-7.61 62.72-21.66-21.61-.41-40.56-14.5-47.18-35.07a50.338 50.338 0 0 0 22.8-.87C27.8 117.2 10.85 96.5 10.85 72.46v-.64a50.18 50.18 0 0 0 22.92 6.32C11.58 63.31 4.74 33.79 18.14 10.71a143.333 143.333 0 0 0 104.08 52.76 50.532 50.532 0 0 1 14.61-48.25c20.34-19.12 52.33-18.14 71.45 2.19 11.31-2.23 22.15-6.38 32.07-12.26a50.69 50.69 0 0 1-22.2 27.93c10.01-1.18 19.79-3.86 29-7.95a102.594 102.594 0 0 1-25.2 26.16z"
        />
      </svg>
    )
  },
  head: () => {
    const { asPath, defaultLocale, locale } = useRouter()
    const { frontMatter } = useConfig()
    const url =
      'https://docs.cogwheel.zone' +
      (defaultLocale === locale ? asPath : `/${locale}${asPath}`)
 
    return (
      <>
        <meta property="og:url" content={url} />
        <meta property="og:title" content={frontMatter.title || 'Cogwheel Validator ⚙️'} />
        <meta
          property="og:description"
          content={frontMatter.description || 'Docs page from Cogwheel Validator!'}
        />
        <meta name="og:image" content="/og_twitter.jpg"/>      
        <meta name="msapplication-TileColor" content="#fff" />
        <meta name="theme-color" content="#fff" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta httpEquiv="Content-Language" content="en" />
        <meta
          name="description"
          content={frontMatter.description || 'Docs page from Cogwheel Validator!'}
        />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:image" content="/public/og_twitter.jpg" />
        <meta name="twitter:site:domain" content="docs.cogwheel.zone" />
        <meta name="twitter:url" content={url} />
        <meta name="apple-mobile-web-app-title" content="Docs Cogwheel" />
        <link rel="icon" href="/favicon.ico" type="image/ico" />
      </>
    )
  },
  feedback: {
    content: null
  },
  sidebar: {
    titleComponent({ title, type }) {
      if (type === 'separator') {
        return <span className="cursor-default">{title}</span>
      }
      return <>{title}</>
    },
    defaultMenuCollapseLevel: 1,
    toggleButton: true
  },
  footer: {
    text: (
      <div className="flex w-full flex-col items-center sm:items-start">
        <p className="mt-6 text-xs">
          © {new Date().getFullYear()} Cogwheel Validator
        </p>
      </div>
    )
  },
  banner: {
    key: 'Docs Page Release',
    text: (
      <span>
        🏗️ Cogwheel's docs page has been released. Some pages need more work and correction. 
      </span>
    )
  },
  toc: {
    backToTop: true
  }
}

export default config
