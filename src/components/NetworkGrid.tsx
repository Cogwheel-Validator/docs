import Link from "next/link";
import Image from "next/image";

export interface NetworkInfo {
    name: string;
    image: string;
    chainId: string;
    networkType: string;
}

interface NetworkGridProps {
    networks: NetworkInfo[];
}

export default function NetworkGrid({ networks }: NetworkGridProps) {
    return (
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
            {networks.map((network) => (
                <div className="flex flex-col items-center justify-center hover:scale-105 transition-all duration-300 active:scale-95" key={network.chainId}>
                    <Link href={`/networks/${network.networkType}/${network.chainId}`}>
                        <Image src={`/icons/${network.image}.png`} alt={`Logo for ${network.name}`} width={100} height={100} loading="eager" className="rounded-full" />
                        <h2>{network.name}</h2>
                        <p>{network.chainId}</p>
                    </Link>
                </div>
            ))}
        </div>
    );
}
