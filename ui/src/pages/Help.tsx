import { useLocation } from "react-router-dom";
import { PageHeader } from "../components/ui";
import { HelpDocument } from "../help/HelpDocument";
import { helpPageFrom, paramsFromPathname } from "../help/paths";
import { locationLabel } from "../shell/nav";

export function HelpPage() {
  const location = useLocation();
  const source = helpPageFrom(location.search, "/");
  const params = paramsFromPathname(source);
  return (
    <div data-testid="help-page">
      <PageHeader title="Documents" />
      <p className="mb-4 text-sm text-stone-500">
        Full-page help for {locationLabel(source)}.
      </p>
      <div className="flex h-[min(70vh,40rem)] min-h-0 flex-col overflow-hidden rounded-2xl border border-stone-200 bg-white p-5">
        <HelpDocument pathname={source} params={params} enabled />
      </div>
    </div>
  );
}
