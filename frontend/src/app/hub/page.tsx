import SectionLayout from "@/components/SectionLayout";
import { Lock, FileText, PackageSearch, MessageSquare } from "lucide-react";

export default function CustomerHub() {
  return (
    <>
      <section className="min-h-screen bg-zinc-950 pt-32 pb-16 flex flex-col items-center justify-center relative overflow-hidden">
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-morris-blue/10 via-zinc-950 to-zinc-950"></div>
        
        <div className="max-w-4xl mx-auto px-4 w-full relative z-10 text-center mb-16">
          <div className="inline-flex items-center justify-center w-20 h-20 bg-zinc-900 border border-zinc-800 rounded-full mb-8">
            <Lock className="w-8 h-8 text-morris-blue" />
          </div>
          <h1 className="text-5xl md:text-7xl font-black text-white uppercase tracking-tighter mb-6">Customer Hub</h1>
          <p className="text-xl text-zinc-400 max-w-2xl mx-auto leading-relaxed">
            The secure portal for managing your active shipments, viewing inventory, and accessing invoices.
          </p>
        </div>

        <div className="w-full max-w-md mx-auto relative z-10">
          <div className="bg-zinc-900 border border-zinc-800 p-8 shadow-2xl">
            <h2 className="text-xl font-black text-white uppercase tracking-tight mb-6">Sign In</h2>
            <form className="space-y-6">
              <div>
                <label className="block text-xs font-bold text-zinc-500 uppercase tracking-widest mb-2">Company Email</label>
                <input type="email" disabled placeholder="admin@company.com" className="w-full bg-zinc-950 border border-zinc-800 px-4 py-3 text-white focus:outline-none focus:border-morris-blue transition-colors disabled:opacity-50" />
              </div>
              <div>
                <label className="block text-xs font-bold text-zinc-500 uppercase tracking-widest mb-2">Password</label>
                <input type="password" disabled placeholder="••••••••" className="w-full bg-zinc-950 border border-zinc-800 px-4 py-3 text-white focus:outline-none focus:border-morris-blue transition-colors disabled:opacity-50" />
              </div>
              <button disabled className="w-full bg-morris-blue text-white font-black uppercase tracking-widest py-4 hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed">
                System Offline
              </button>
            </form>
            <div className="mt-6 text-center">
              <p className="text-xs text-zinc-500 uppercase tracking-widest">Client portals are currently undergoing scheduled maintenance. Please contact your account manager for immediate assistance.</p>
            </div>
          </div>
        </div>

        <div className="max-w-7xl mx-auto px-4 w-full relative z-10 mt-32">
          <h3 className="text-center text-sm font-bold text-zinc-600 uppercase tracking-[0.2em] mb-12">Future Capabilities</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 opacity-50">
            <div className="border border-zinc-800 p-6 bg-zinc-900/50 flex flex-col items-center text-center">
              <PackageSearch className="w-8 h-8 text-zinc-500 mb-4" />
              <h4 className="text-white font-black uppercase tracking-tight mb-2">Live Tracking</h4>
              <p className="text-xs text-zinc-400">Real-time status updates on crating and transit.</p>
            </div>
            <div className="border border-zinc-800 p-6 bg-zinc-900/50 flex flex-col items-center text-center">
              <FileText className="w-8 h-8 text-zinc-500 mb-4" />
              <h4 className="text-white font-black uppercase tracking-tight mb-2">Invoice Portal</h4>
              <p className="text-xs text-zinc-400">Download and manage billing documents securely.</p>
            </div>
            <div className="border border-zinc-800 p-6 bg-zinc-900/50 flex flex-col items-center text-center">
              <MessageSquare className="w-8 h-8 text-zinc-500 mb-4" />
              <h4 className="text-white font-black uppercase tracking-tight mb-2">AI Support</h4>
              <p className="text-xs text-zinc-400">Instant answers regarding packing requirements and status.</p>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
