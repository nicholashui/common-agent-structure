Update and refine the chat system at http://localhost:15173/projects/asain-beauty/chat to fully implement the autonomous agent swarm "Auto Pilot" architecture as outlined below:

1. First, resolve and clean up the existing duplicated and malformed human role assignments in the chat: standardize the valid domain-specific human agent roles to "Human → video.promptengineer", "Human → video.director", "Human → video.cinematographer", "Human → video.mua_makeup", "Human → video.continuity", removing all duplicate entries and formatting errors.

2. Re-architect the workflow to align with the core "Auto Pilot" model:
   - The human user only needs to provide initial draft project information, rather than writing detailed, domain-specific prompts directly for each agent.
   - Implement and deploy the intent-analysis-agent that accurately interprets and infers the human user’s core project requirements and objectives from the draft input.
   - Activate the newly developed creative-agent that generates innovative, actionable project concepts and execution frameworks aligned with the interpreted intent.
   - Enable all domain-specific agents (video.promptengineer, video.director, video.cinematographer, video.mua_makeup, video.continuity) to leverage their specialized domain knowledge to refine outputs, maintain cross-agent consistency across every iteration, and communicate collaboratively with one another.
   - Build an interactive agent-to-human question system: agents will proactively surface clarifying questions to the human user, each paired with pre-vetted, domain-aligned suggested answers, so the human user only needs to select options rather than draft responses from scratch.
   - Implement an iterative loop mechanism that allows the agent swarm to cycle through intent analysis, creative ideation, domain refinement, and human confirmation multiple times until the project is fully realized, transitioning the swarm to full "Auto Pilot" operation once sufficient aligned iterations are completed.

3. Update all chat interfaces, message flows, and agent communication protocols to support this new architecture end-to-end.

4. Push the implementation to exceed baseline requirements: rethink core agent interaction logic to eliminate inefficiencies, work to resolve any unaddressed gaps in the current workflow, and add enhanced creative functionality to the creative-agent and domain-specific agents to produce more robust, innovative project outcomes. Finalize all updates to complete the full system implementation.