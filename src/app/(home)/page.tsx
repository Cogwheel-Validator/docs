import Link from "next/link";
import Image from "next/image";

export default function HomePage() {
  return (
    <main className="flex flex-1 flex-col justify-center text-center">
      <Image
          src="/main-page/cover.jpg"
          alt="Cogwheel Docs"
          width={1920}
          height={1080}
          className="max-h-96 w-auto mx-auto object-contain"
        />
      <h1 className="">Welcome to Cogwheel's Docs Page!</h1>
      <p className="text-fd-muted-foreground">
        You can open{" "}
        <Link
          href="/docs"
          className="text-fd-foreground font-semibold underline"
        >
          /docs
        </Link>{" "}
        and see the documentation.
      </p>
    </main>
  );
}
