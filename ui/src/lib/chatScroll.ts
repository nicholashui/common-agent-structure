export function distanceFromBottom(el: HTMLElement): number {
  return el.scrollHeight - el.scrollTop - el.clientHeight;
}

export function isPinnedToBottom(el: HTMLElement, threshold = 80): boolean {
  return distanceFromBottom(el) <= threshold;
}
