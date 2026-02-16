import type { BaseLayoutProps } from "fumadocs-ui/layouts/shared";
import Image from "next/image";

/**
 * Shared layout configurations
 *
 * you can customise layouts individually from:
 * Home Layout: app/(home)/layout.tsx
 * Docs Layout: app/docs/layout.tsx
 */
export const baseOptions: BaseLayoutProps = {
  nav: {
    title: (
      <>
        <Image
          src="/logo-dark.png"
          alt="Cogwheel Docs"
          width={32}
          height={32}
          loading="eager"
        />
        <span className="text-xl font-bold text-fd-foreground">
          Cogwheel Docs
        </span>
      </>
    ),
  },
};

/**
 * Home page specific configuration with navigation menus
 */
export const homeOptions: BaseLayoutProps = {
  nav: {
    title: (
      <>
        <Image
          src="/logo-dark.png"
          alt="Cogwheel Docs"
          width={32}
          height={32}
          loading="eager"
        />
        <span className="text-xl font-bold text-fd-foreground">
          Cogwheel Docs
        </span>
      </>
    ),
  },
  // see https://fumadocs.dev/docs/ui/navigation/links
  links: [
    {
      type: "menu",
      text: "Networks",
      items: [
        {
          text: "Mainnets",
          description: "Node guide for mainnets",
          url: "/networks/mainnets",
          icon: "🌐"
        },
        {
          text: "Testnets",
          description: "Node guide for testnets",
          url: "/networks/testnets",
          icon: "🌐",
        },
      ],
    },
    {
      type: "menu",
      text: "Services",
      items: [
        { text: "Restake", url: "/services/restake"},
        { text: "Dyson Frontend", url: "/services/frontend" },
        { text: "Explorer", url: "/services/explorer"},
        { text: "Chain Endpoints", url: "/services/endpoints"},
      ],
      icon: "🔧",
    },
    {
      text: "Spectra Portal",
      url: "/spectra-portal",
    }
  ],
};
