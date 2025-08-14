import Image from "next/image";

export default function HomePage() {
  return (
    <main className="flex flex-1 flex-col justify-center text-center">
      <Image src="/logo1.png" alt="Cogwheel Logo" width={200} height={200} />
      <h1 className="">Welcome to Cogwheel&apos;s Docs Page!</h1>
      <p className="text-fd-muted-foreground">
        Need a help setting up blockchain node? Or do you need to understand how some of our services work?<br/>
        Then you are in the right place!
      </p>
    </main>
  );
}
