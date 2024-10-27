import React from "react";
import {Card, CardBody, CardFooter, Image} from "@nextui-org/react";
import { useRouter } from "next/router";

export default function testnet() {
    const router = useRouter();
    const list = [
      {
        title: "Blit Chain",
        img: "/icons/blitIcon.png",
        chainID: "blit-testnet-1",
        href:"./testnet/blit-chain"
      },
      {
        title: "Composable Cosmos",
        img: "/icons/composableIcon.png",
        chainID: "banksy-testnet-5",
        href: "./testnet/composable-cosmos"
      },
      {
        title: "Babylon Chain",
        img: "/icons/babylonIcon.png",
        chainID: "bbn-test-3",
        href: "./testnet/babylon-chain"
      },
      {
        title: "Side Protocol",
        img: "/icons/sideIcon.png",
        chainID: "S2-testnet-2",
        href: "./testnet/side-protocol"
      },
      {
        title: "Union Network",
        img: "/icons/unionIcon.png",
        chainID: "union-testnet-8",
        href: "./testnet/union-network"
      },
      {
        title: "Juno Testnet",
        img: "/icons/junoIcon.png",
        chainID: "uni-6",
        href: "./testnet/juno"
      },
      {
        title: "Initia Testnet",
        img: "/icons/initiaIcon.png",
        chainID: "initiation-1",
        href: "./testnet/initia"
      },
      {
        title: "Symphony Testnet",
        img: "/icons/symphonyIcon.png",
        chainID: "symphony-testnet-3",
        href: "./testnet/symphony-testnet"
      },
      {
        title: "Prysm Devnet",
        img: "/icons/prysmIcon.png",
        chainID: "prysm-devnet-1",
        href: "./testnet/prysm"
      },
    ];
  
    return (
      <div className="grid grid-cols-2 gap-2 sm:grid-cols-4">
        {list.map((item, index) => (
          <Card
          shadow='sm'
          key={index}
          isPressable
          onPress={() => router.push(item.href)} // Use the router to navigate when the card is pressed
          style={{ margin: '10px' }}
        >
            <CardBody className="p-0 overflow-visible">
              <Image
                shadow="sm"
                radius="lg"
                width="100%"
                alt={item.title}
                className="w-full object-cover h-[140px]"
                src={item.img}
              />
            </CardBody>
            <CardFooter className="justify-between text-small">
              <b>{item.title}</b>
              <p className="text-default-500">{item.chainID}</p>
            </CardFooter>
          </Card>
        ))}
      </div>
    );
        }
  
  