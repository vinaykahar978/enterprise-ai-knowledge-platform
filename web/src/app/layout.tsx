import "./globals.css";

export const metadata = {
  title: "Enterprise AI Platform",
  description: "Internal AI Knowledge Platform",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-slate-50 text-slate-900 antialiased">
        <div className="flex min-h-screen">
          {/* Sidebar */}
          <aside className="w-64 bg-white border-r border-slate-200 flex flex-col">
            <div className="px-6 py-5 border-b border-slate-200">
              <h2 className="text-lg font-semibold tracking-tight">
                Enterprise AI
              </h2>
              <p className="text-xs text-slate-500 mt-1">
                Knowledge & Decision Platform
              </p>
            </div>

            <nav className="flex-1 px-4 py-6 space-y-1 text-sm">
              <a
                href="/"
                className="block rounded-md px-3 py-2 hover:bg-slate-100 transition"
              >
                Ask
              </a>

              <a
                href="/upload"
                className="block rounded-md px-3 py-2 hover:bg-slate-100 transition"
              >
                Upload Documents
              </a>

              <a
                href="/admin"
                className="block rounded-md px-3 py-2 hover:bg-slate-100 transition"
              >
                Admin & Observability
              </a>
            </nav>

            <div className="px-6 py-4 border-t border-slate-200 text-xs text-slate-500">
              © Internal Platform
            </div>
          </aside>

          {/* Main Content */}
          <main className="flex-1 p-8 max-w-6xl mx-auto w-full">
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}
