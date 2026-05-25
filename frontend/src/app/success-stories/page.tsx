import SectionLayout from "@/components/SectionLayout";
import Image from "next/image";
import { ArrowRight } from "lucide-react";

export default function SuccessStories() {
  const stories = [
    {
      client: "Global Petrochemical",
      title: "Delta Refinery Expansion",
      metric: "40+ Oversized Units",
      img: "/images/containerization/container1.webp",
      desc: "Managed the transloading, securing, and export packing of massive refinery components destined for South America. Zero incidents, delivered ahead of schedule."
    },
    {
      client: "Aerospace Defense",
      title: "Fragile Instrumentation Transport",
      metric: "Shock-proof Crating",
      img: "/images/mpacttech/mpact2.webp",
      desc: "Engineered specialized vapor-barrier and shock-absorbing crates for highly sensitive satellite instrumentation."
    },
    {
      client: "Heavy Manufacturing",
      title: "Factory Relocation",
      metric: "Turnkey Operation",
      img: "/images/facilityrelocation/facilityrelocation].webp",
      desc: "Dismantled, packed, and transported an entire manufacturing line from Texas to Mexico. Coordinated heavy haul, crating, and border logistics."
    }
  ];

  return (
    <>
      <section className="pt-32 pb-16 bg-zinc-950 border-b border-zinc-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 className="text-5xl md:text-7xl font-black text-white uppercase tracking-tighter mb-6">Success Stories</h1>
          <p className="text-xl text-zinc-400 max-w-3xl leading-relaxed">
            Case studies demonstrating our capacity to handle the most demanding logistical challenges across the energy, manufacturing, and defense sectors.
          </p>
        </div>
      </section>

      <SectionLayout>
        <div className="space-y-24">
          {stories.map((story, idx) => (
            <div key={idx} className={`flex flex-col ${idx % 2 === 0 ? 'lg:flex-row' : 'lg:flex-row-reverse'} gap-12 items-center`}>
              <div className="w-full lg:w-1/2 relative h-[400px] border border-zinc-800 p-2 bg-zinc-900">
                <div className="relative w-full h-full overflow-hidden">
                  <Image src={story.img} alt={story.title} fill className="object-cover grayscale hover:grayscale-0 transition-all duration-700" />
                </div>
                <div className="absolute -bottom-6 -right-6 bg-morris-blue p-6 shadow-xl hidden md:block">
                  <div className="text-white font-black uppercase tracking-widest text-sm">{story.metric}</div>
                </div>
              </div>
              <div className="w-full lg:w-1/2">
                <h3 className="text-morris-red font-bold text-sm tracking-[0.2em] uppercase mb-4">{story.client}</h3>
                <h2 className="text-3xl md:text-4xl font-black uppercase tracking-tight text-white mb-6">{story.title}</h2>
                <p className="text-zinc-400 text-lg leading-relaxed mb-8">{story.desc}</p>
                <button className="flex items-center text-sm font-bold uppercase tracking-widest text-white hover:text-morris-blue transition-colors group">
                  Read Full Study <ArrowRight className="ml-2 w-4 h-4 group-hover:translate-x-1 transition-transform" />
                </button>
              </div>
            </div>
          ))}
        </div>
      </SectionLayout>
    </>
  );
}
