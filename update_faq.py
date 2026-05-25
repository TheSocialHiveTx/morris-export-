import sys

file_path = r'c:\Users\suppo\OneDrive\Desktop\Developer\morris-export-\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update FAQ
start_faq = content.find('function renderFAQ() {')
end_faq = content.find('function renderOurTeam() {')

faq_new = '''function renderFAQ() {
      const faqs = [
        { q: "What is an NCB inspection?", a: "An NCB inspection is an inspection conducted by National Cargo Bureau. Many shippers now require that Flat Racks be inspected prior to being loaded onto the vessel. Morris will handle all aspects of the inspection including scheduling." },
        { q: "Is Morris a 'Bonded' facility?", a: "Yes. Morris operates bonded warehouse capabilities and follows U.S. Customs procedures for bonded cargo handling and storage." },
        { q: "Is Morris C-TPAT Certified?", a: "Morris follows strict cargo security and compliance procedures. For current C-TPAT status and documentation requirements, please contact our team directly." },
        { q: "Does Morris pack air freight?", a: "Yes. We provide export packing and crating solutions suitable for air freight shipments, including weight-conscious and carrier-compliant packaging options." },
        { q: "Does Morris have their own trucks?", a: "Yes. Morris provides trucking and drayage support, including Port of Houston moves and specialized transport coordination for oversized cargo." },
        { q: "Can Morris receive rail freight?", a: "Yes, we can coordinate receiving for rail-delivered cargo. Contact operations in advance so unloading and scheduling requirements can be arranged." },
        { q: "Can Morris pack Hazardous Materials?", a: "Yes. We provide hazardous material packaging services with appropriate handling and documentation based on shipment class and destination requirements." },
        { q: "Can Morris pack offsite at either a vendor facility or at the local area docks?", a: "Yes. Our mobile teams can perform offsite packing at customer or vendor facilities and can also support packing activities at local dock locations when scheduled." },
        { q: "Is Morris' wood IPPC compliant?", a: "Yes. Morris uses ISPM-15 / IPPC-compliant heat-treated wood for export crating where required for international shipments." },
        { q: "How long does it take to pack material once received?", a: "Turnaround depends on cargo type, dimensions, and project scope. Standard jobs are often completed quickly; complex projects are scheduled with a detailed production timeline." },
        { q: "Does Morris provide moisture-sensitive packing?", a: "Yes. We offer moisture-control solutions including VCI materials, desiccants, barrier wrapping, and sealed protection systems for sensitive equipment." },
        { q: "Do Morris offsite employees have TWIC cards?", a: "Yes. Personnel assigned to applicable port and secure areas maintain required credentials, including TWIC, as needed for site access." },
        { q: "What is a TWIC card and what is it used for?", a: "A TWIC (Transportation Worker Identification Credential) card is a federal security credential required for unescorted access to secure maritime and port facilities." },
        { q: "What are Morris' receiving hours?", a: "Standard receiving is handled during normal business hours. For exact receiving windows and after-hours coordination, please contact our operations team before delivery." },
        { q: "Does Morris have a secured facility?", a: "Yes. Our facility uses controlled access and active security measures to protect customer cargo, equipment, and documentation." },
        { q: "Compliance Bulletin: Price Transparency", a: "Machine-readable file information for applicable price transparency requirements is available upon request. Contact our office for access details." }
      ];

      const faqHtml = faqs.map(item => `
                <details class="bg-white border border-zinc-200 rounded-[1.5rem] group overflow-hidden shadow-sm hover:shadow-md transition-all mb-4" ${item.q === 'What is an NCB inspection?' ? 'open' : ''}>
                    <summary class="list-none cursor-pointer px-6 md:px-8 py-6 flex items-center justify-between gap-4 text-zinc-900 font-bold text-lg hover:text-morris-blue transition-colors">
                        <span>${item.q}</span>
                        <div class="w-10 h-10 bg-zinc-50 rounded-full flex items-center justify-center shrink-0 group-open:bg-blue-50 group-open:text-morris-blue transition-colors">
                            <i data-lucide="chevron-down" class="w-5 h-5 shrink-0 group-open:rotate-180 transition-transform"></i>
                        </div>
                    </summary>
                    <div class="px-6 md:px-8 pb-8 pt-2 text-zinc-600 leading-relaxed text-base">
                        ${item.a}
                    </div>
                </details>
            `).join('');

      return `
                <div class="pt-20">
                    <section class="py-24 bg-zinc-50">
                        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
                            <div class="text-center mb-16">
                                <div class="w-16 h-16 bg-blue-100 text-morris-blue rounded-2xl flex items-center justify-center mx-auto mb-6">
                                    <i data-lucide="help-circle" class="w-8 h-8"></i>
                                </div>
                                <h1 class="text-5xl font-black tracking-tighter uppercase text-zinc-900 mb-6">Frequently Asked Questions</h1>
                                <p class="text-lg text-zinc-600">Find answers to common questions about our services, certifications, and operational procedures.</p>
                            </div>
                            <div class="space-y-4">
                                ${faqHtml}
                            </div>
                        </div>
                    </section>
                </div>
            `;
    }
'''
if start_faq != -1 and end_faq != -1:
    content = content[:start_faq] + faq_new + content[end_faq:]


# 2. Update Credit App
start_credit = content.find('function renderCreditApplication() {')
end_credit = content.find('function renderFAQ() {')

credit_new = '''function renderCreditApplication() {
      return `
                <div class="pt-20">
                    <section class="relative h-[30vh] flex items-center overflow-hidden">
                        <div class="absolute inset-0 z-0">
                            <img src="images/warehousemanagement/warehousepackaging2.webp" class="w-full h-full object-cover grayscale opacity-20" alt="Background">
                            <div class="absolute inset-0 bg-zinc-950"></div>
                        </div>
                        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full text-center pt-8">
                            <h1 class="text-4xl md:text-5xl font-black text-white uppercase tracking-tighter mb-4">Credit Application</h1>
                            <p class="text-zinc-400">Establish your account with Morris Export Services.</p>
                        </div>
                    </section>

                    <section class="py-16 bg-zinc-50 relative -mt-10 z-20 rounded-t-[3rem]">
                        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
                            <div class="bg-white p-8 md:p-12 rounded-[2rem] border border-zinc-200 shadow-xl">
                                <div class="flex items-center gap-4 mb-8 pb-8 border-b border-zinc-100">
                                    <div class="w-12 h-12 bg-blue-50 text-morris-blue rounded-xl flex items-center justify-center">
                                        <i data-lucide="file-text" class="w-6 h-6"></i>
                                    </div>
                                    <div>
                                        <h2 class="text-2xl font-black uppercase text-zinc-900">Application Form</h2>
                                        <p class="text-sm text-zinc-500">Please complete all fields below to apply for credit.</p>
                                    </div>
                                </div>
                                <div class="text-center py-16">
                                    <i data-lucide="wrench" class="w-16 h-16 text-zinc-300 mx-auto mb-6"></i>
                                    <h3 class="text-xl font-bold text-zinc-800 mb-2">Digital Application Form</h3>
                                    <p class="text-zinc-500 mb-8 max-w-md mx-auto">Our interactive digital credit application is currently being updated to provide a better experience. In the meantime, please contact our billing department directly.</p>
                                    <a href="mailto:billing@morris-export.com" class="inline-flex items-center justify-center bg-morris-blue text-white font-bold uppercase tracking-widest px-8 py-4 rounded-xl hover:bg-blue-700 transition-colors shadow-lg shadow-blue-900/20">
                                        Email Billing Department <i data-lucide="mail" class="w-5 h-5 ml-3"></i>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </section>
                </div>
            `;
    }
'''
if start_credit != -1 and end_credit != -1:
    content = content[:start_credit] + credit_new + content[end_credit:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
