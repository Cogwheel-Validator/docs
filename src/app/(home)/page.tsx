import Link from "next/link";
import Image from "next/image";

export default function HomePage() {
  return (
    <main className="flex flex-1 flex-col justify-center text-center">
      <h1 className="">Welcome to Cogwheel's Docs Page!</h1>
      <p className="text-fd-muted-foreground">
        Need a help setting up blockchain node? Or do you need to understand how some of our services work?<br/>
        Then you are in the right place!
      </p>
    </main>
  );
}
