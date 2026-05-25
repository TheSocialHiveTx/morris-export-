"use client";
import { motion } from "framer-motion";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import Image from "next/image";

interface ServiceCardProps {
  title: string;
  description: string;
  image: string;
  link: string;
}

export default function ServiceCard({ title, description, image, link }: ServiceCardProps) {
  return (
    <Link href={link} className="group block">
      <motion.div 
        whileHover={{ y: -5 }}
        className="industrial-card overflow-hidden h-full flex flex-col group-hover:border-morris-blue/50 transition-colors duration-300"
      >
        <div className="relative h-48 sm:h-64 overflow-hidden bg-zinc-950">
          {/* Fallback pattern if image is missing, but Next/Image requires real src */}
          <Image 
            src={image} 
            alt={title} 
            fill
            className="object-cover opacity-70 group-hover:opacity-100 group-hover:scale-105 transition-all duration-700"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-zinc-950 via-zinc-950/20 to-transparent"></div>
          
          <div className="absolute bottom-4 left-6">
            <h3 className="text-xl font-black uppercase tracking-tight text-white">{title}</h3>
            <div className="w-8 h-1 bg-morris-red mt-2 group-hover:w-full transition-all duration-500"></div>
          </div>
        </div>
        
        <div className="p-6 flex-grow flex flex-col">
          <p className="text-zinc-400 text-sm leading-relaxed mb-6 flex-grow">
            {description}
          </p>
          
          <div className="flex items-center text-xs font-bold uppercase tracking-widest text-morris-blue group-hover:text-white transition-colors">
            Learn More <ArrowRight className="ml-2 w-4 h-4" />
          </div>
        </div>
      </motion.div>
    </Link>
  );
}
