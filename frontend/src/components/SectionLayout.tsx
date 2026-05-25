interface SectionLayoutProps {
  children: React.ReactNode;
  title?: string;
  subtitle?: string;
  dark?: boolean;
  className?: string;
}

export default function SectionLayout({ children, title, subtitle, dark = false, className = "" }: SectionLayoutProps) {
  return (
    <section className={`py-24 ${dark ? "bg-zinc-950" : "bg-zinc-900"} ${className}`}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {(title || subtitle) && (
          <div className="mb-16 md:mb-20">
            {subtitle && (
              <h3 className="text-morris-red font-bold text-sm tracking-[0.2em] uppercase mb-4 flex items-center gap-4">
                <span className="w-8 h-px bg-morris-red"></span>
                {subtitle}
              </h3>
            )}
            {title && (
              <h2 className="text-4xl md:text-5xl font-black uppercase tracking-tighter text-white">
                {title}
              </h2>
            )}
          </div>
        )}
        {children}
      </div>
    </section>
  );
}
