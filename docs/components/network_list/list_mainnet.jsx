import React from "react";
import {Card, CardBody, CardFooter, Image} from "@nextui-org/react";
import { useRouter } from "next/router";

export default function mainnet() {
  const router = useRouter();
  const list = [
    {
      title: "Blit Chain",
      img: "/icons/blitIcon.png",
      chainID: "blit-1",
      href:"./mainnet/blit-chain"
    },
    {
      title: "Picasso Cosmos",
      img: "/icons/picassoIcon.png",
      chainID: "centauri-1",
      href: "./mainnet/picasso-cosmos"
    },
    {
      title: "Dyson Protocol",
      img: "/icons/dysonIcon.png",
      chainID: "dyson-mainnet-01",
      href: "./mainnet/dyson-protocol"
    },
    {
      title: "Juno Network",
      img: "/icons/junoIcon.png",
      chainID: "juno-1",
      href: "./mainnet/juno-network"
    },
    {
      title: "Nibiru Chain",
      img: "/icons/nibiruIcon.png",
      chainID: "cataclysm-1",
      href: "./mainnet/nibiru"
    },
    {
      title: "Saga Protocol",
      img: "/icons/sagaIcon.png",
      chainID: "ssc-1",
      href: "./mainnet/saga"
    }
  ];

  return (
    <div className="gap-2 grid grid-cols-2 sm:grid-cols-4">
      {list.map((item, index) => (
        <Card
        shadow='sm'
        key={index}
        isPressable
        onPress={() => router.push(item.href)} // Use the router to navigate when the card is pressed
        style={{ margin: '10px' }}
      >
          <CardBody className="overflow-visible p-0">
            <Image
              shadow="sm"
              radius="lg"
              width="100%"
              alt={item.title}
              className="w-full object-cover h-[140px]"
              src={item.img}
            />
          </CardBody>
          <CardFooter className="text-small justify-between">
            <b>{item.title}</b>
            <p className="text-default-500">{item.chainID}</p>
          </CardFooter>
        </Card>
      ))}
    </div>
  );
      }
