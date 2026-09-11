import { MarkdownBody } from "./MarkdownBody";

export function ChatMarkdown({ text }: { text: string }) {
  return <MarkdownBody text={text} className="md-body-chat" />;
}
