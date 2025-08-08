import { JSX } from "react";
import { 
    Info,
    CheckCheck,
    MessageSquareWarning,
    ShieldX 
} from 'lucide-react';
interface CalloutProps {
    type: "info" | "warning" | "error" | "success";
    text: string;
}

export default function Callout({ type, text }: CalloutProps): JSX.Element {
    const bgColor = type === "info" ? "bg-indigo-400 ring-indigo-700" :
    type === "warning" ? "bg-yellow-400 ring-yellow-700" :
    type === "error" ? "bg-red-400 ring-red-700" :
    type === "success" ? "bg-green-400 ring-green-700" :
    "bg-indigo-400 ring-indigo-700";
    return (
        <div className={`ring-4 rounded-xl p-2 flex flex-row space-x-2 items-center ${bgColor}`}>
            {type === "info" && <Info className="w-16 h-16 text-indigo-900" />}
            {type === "warning" && <MessageSquareWarning className="w-16 h-16 text-yellow-900" />}
            {type === "error" && <ShieldX className="w-16 h-16 text-red-900" />}
            {type === "success" && <CheckCheck className="w-16 h-16 text-green-900" />}
            <p className={`${type === "info" ? "text-indigo-900" : type === "warning" ? "text-yellow-900" : type === "error" ? "text-red-900" : type === "success" ? "text-green-900" : ""}`}>{text}</p>
        </div>
    )
}