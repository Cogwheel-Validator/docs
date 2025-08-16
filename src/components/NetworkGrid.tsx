import Link from "next/link";
import Image from "next/image";

export interface NetworkInfo {
    name: string;
    image: string;
    chainId: string;
    networkType: string;
    path: string;
}

interface NetworkGridProps {
    networks: NetworkInfo[];
}

export default function NetworkGrid({ networks }: NetworkGridProps) {
    return (
        <div className="grid grid-cols-2 lg:grid-cols-3 gap-4 justify-items-center">
            {networks.map((network) => (
                <div className="hover:scale-105 transition-all duration-300 active:scale-95" key={network.chainId}>
                    <Link href={`/networks/${network.networkType}s/${network.path}`} className="flex flex-col items-center justify-center ">
                        <Image src={`/icons/${network.image}.png`} alt={`Logo for ${network.name}`} width={100} height={100} loading="eager" className="rounded-full not-prose mt-1" />
                        <h2 className="text-center p-0.25 not-prose mt-0.5">{network.name}</h2>
                        <p className="text-center p-0.25 not-prose">{network.chainId}</p>
                    </Link>
                </div>
            ))}
        </div>
    );
}
