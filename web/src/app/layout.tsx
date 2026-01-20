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
      <body className="bg-gray-100 text-gray-900">
        <div className="flex min-h-screen">
          <aside className="w-64 bg-white border-r p-4">
            <h2 className="font-semibold text-lg mb-6">
              AI Platform
            </h2>
            <nav className="space-y-2">
              <a href="/" className="block text-sm hover:underline">
                Ask
              </a>
              <a href="/upload" className="block text-sm hover:underline">
                Upload Docs
              </a>
            </nav>
          </aside>

          <main className="flex-1 p-8">
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}
