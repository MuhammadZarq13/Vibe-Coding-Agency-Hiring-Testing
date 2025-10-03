# Agent Orchestration for Cloud Architecture Planning
# Format: Problem statement + Written response

"""
AGENT ORCHESTRATION CHALLENGE

You need to design a multi-agent system that can analyze business problems and recommend 
cloud architecture solutions. Focus on the orchestration strategy, not implementation details.

SAMPLE SCENARIOS (choose 2 to address):

1. "Simple E-commerce Site"
   - Online store for small business (1000 daily users)
   - Product catalog, shopping cart, payment processing
   - Basic admin dashboard for inventory management

2. "Customer Support Chatbot"
   - AI chatbot for customer service 
   - Integration with existing CRM system
   - Handle 500+ conversations per day
   - Escalate complex issues to human agents

3. "Employee Expense Tracker"
   - Mobile app for expense reporting
   - Receipt photo upload and processing
   - Approval workflow for managers
   - Integration with payroll system

YOUR TASK:
Design an agent orchestration approach that can take these problems and output 
a cloud architecture recommendation including basic services needed (database, 
API gateway, compute, storage, etc.).
"""

# Multi-Agent Cloud Architecture Planning System

import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum
import asyncio
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ArchitectureType(Enum):
    ECOMMERCE = "ecommerce"
    CHATBOT = "chatbot"
    EXPENSE_TRACKER = "expense_tracker"

class CloudProvider(Enum):
    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"

@dataclass
class BusinessRequirement:
    """Represents a business requirement for cloud architecture"""
    description: str
    priority: int  # 1-5, 5 being highest
    category: str  # performance, security, scalability, cost, compliance
    constraints: List[str]

@dataclass
class TechnicalRequirement:
    """Represents a technical requirement for cloud architecture"""
    component: str
    requirements: List[str]
    dependencies: List[str]
    performance_needs: Dict[str, Any]

@dataclass
class CloudService:
    """Represents a cloud service recommendation"""
    name: str
    provider: CloudProvider
    service_type: str  # compute, storage, database, networking, security
    description: str
    cost_estimate: str
    scalability: str
    security_features: List[str]

@dataclass
class ArchitectureRecommendation:
    """Complete architecture recommendation"""
    architecture_type: ArchitectureType
    services: List[CloudService]
    deployment_strategy: str
    cost_estimate: str
    security_considerations: List[str]
    scalability_plan: str
    monitoring_strategy: str
    confidence_score: float

class RequirementsAnalyzer:
    """Agent responsible for analyzing business requirements"""
    
    def __init__(self):
        self.name = "Requirements Analyzer"
        self.expertise = ["business analysis", "requirement gathering", "stakeholder communication"]
    
    async def analyze_requirements(self, problem_description: str) -> Dict[str, Any]:
        """Analyze business problem and extract requirements"""
        logger.info(f"{self.name}: Analyzing requirements for: {problem_description}")
        
        # Parse the problem description to extract key requirements
        requirements = {
            "business_requirements": [],
            "technical_requirements": [],
            "constraints": [],
            "success_metrics": []
        }
        
        # Extract business requirements based on problem type
        if "ecommerce" in problem_description.lower():
            requirements["business_requirements"] = [
                BusinessRequirement("Handle 1000 daily users", 5, "scalability", ["high_availability"]),
                BusinessRequirement("Secure payment processing", 5, "security", ["PCI_DSS_compliance"]),
                BusinessRequirement("Product catalog management", 4, "functionality", ["search_capability"]),
                BusinessRequirement("Shopping cart functionality", 4, "functionality", ["session_management"]),
                BusinessRequirement("Admin dashboard", 3, "functionality", ["user_management"])
            ]
            requirements["technical_requirements"] = [
                TechnicalRequirement("web_application", ["responsive_design", "mobile_support"], [], {"response_time": "<2s"}),
                TechnicalRequirement("database", ["ACID_compliance", "backup_recovery"], ["web_application"], {"concurrent_users": 1000}),
                TechnicalRequirement("payment_gateway", ["PCI_compliance", "encryption"], ["web_application"], {"transaction_volume": "high"}),
                TechnicalRequirement("file_storage", ["image_optimization", "CDN"], ["web_application"], {"storage_capacity": "unlimited"})
            ]
            requirements["constraints"] = ["budget_conscious", "time_to_market"]
            requirements["success_metrics"] = ["user_satisfaction", "conversion_rate", "uptime"]
            
        elif "chatbot" in problem_description.lower():
            requirements["business_requirements"] = [
                BusinessRequirement("Handle 500+ conversations daily", 5, "scalability", ["real_time_processing"]),
                BusinessRequirement("CRM integration", 4, "integration", ["api_compatibility"]),
                BusinessRequirement("Human escalation", 3, "functionality", ["seamless_handoff"]),
                BusinessRequirement("Multi-language support", 3, "functionality", ["internationalization"])
            ]
            requirements["technical_requirements"] = [
                TechnicalRequirement("ai_service", ["natural_language_processing", "sentiment_analysis"], [], {"response_time": "<1s"}),
                TechnicalRequirement("conversation_storage", ["real_time_access", "privacy_compliance"], ["ai_service"], {"concurrent_conversations": 500}),
                TechnicalRequirement("crm_integration", ["api_connectivity", "data_sync"], ["ai_service"], {"sync_frequency": "real_time"})
            ]
            requirements["constraints"] = ["ai_model_accuracy", "response_time"]
            requirements["success_metrics"] = ["resolution_rate", "customer_satisfaction", "escalation_rate"]
            
        elif "expense" in problem_description.lower():
            requirements["business_requirements"] = [
                BusinessRequirement("Mobile app support", 5, "functionality", ["cross_platform"]),
                BusinessRequirement("Receipt photo processing", 4, "functionality", ["ocr_capability"]),
                BusinessRequirement("Approval workflow", 4, "functionality", ["notification_system"]),
                BusinessRequirement("Payroll integration", 3, "integration", ["secure_data_transfer"])
            ]
            requirements["technical_requirements"] = [
                TechnicalRequirement("mobile_backend", ["rest_api", "authentication"], [], {"concurrent_users": 500}),
                TechnicalRequirement("image_processing", ["ocr_service", "image_storage"], ["mobile_backend"], {"processing_time": "<5s"}),
                TechnicalRequirement("workflow_engine", ["approval_routing", "notifications"], ["mobile_backend"], {"approval_time": "<24h"}),
                TechnicalRequirement("payroll_integration", ["secure_api", "data_validation"], ["workflow_engine"], {"sync_frequency": "daily"})
            ]
            requirements["constraints"] = ["mobile_performance", "data_privacy"]
            requirements["success_metrics"] = ["user_adoption", "processing_accuracy", "approval_efficiency"]
        
        return requirements

class CloudArchitect:
    """Agent responsible for designing cloud architecture"""
    
    def __init__(self):
        self.name = "Cloud Architect"
        self.expertise = ["cloud_design", "scalability", "cost_optimization", "multi_cloud"]
    
    async def design_architecture(self, requirements: Dict[str, Any], preferred_provider: CloudProvider = CloudProvider.AWS) -> ArchitectureRecommendation:
        """Design cloud architecture based on requirements"""
        logger.info(f"{self.name}: Designing architecture for {preferred_provider.value}")
        
        services = []
        
        # Design based on architecture type
        if any("ecommerce" in req.description.lower() for req in requirements["business_requirements"]):
            services = self._design_ecommerce_architecture(preferred_provider)
        elif any("chatbot" in req.description.lower() for req in requirements["business_requirements"]):
            services = self._design_chatbot_architecture(preferred_provider)
        elif any("expense" in req.description.lower() for req in requirements["business_requirements"]):
            services = self._design_expense_tracker_architecture(preferred_provider)
        
        return ArchitectureRecommendation(
            architecture_type=ArchitectureType.ECOMMERCE,  # This would be determined dynamically
            services=services,
            deployment_strategy=self._get_deployment_strategy(requirements),
            cost_estimate=self._estimate_costs(services),
            security_considerations=self._get_security_considerations(requirements),
            scalability_plan=self._get_scalability_plan(requirements),
            monitoring_strategy=self._get_monitoring_strategy(requirements),
            confidence_score=0.85
        )
    
    def _design_ecommerce_architecture(self, provider: CloudProvider) -> List[CloudService]:
        """Design ecommerce architecture"""
        if provider == CloudProvider.AWS:
            return [
                CloudService("Amazon EC2", CloudProvider.AWS, "compute", "Web application servers", "$200-500/month", "Auto Scaling", ["VPC", "Security Groups"]),
                CloudService("Amazon RDS", CloudProvider.AWS, "database", "MySQL/PostgreSQL database", "$100-300/month", "Read replicas", ["Encryption at rest", "VPC"]),
                CloudService("Amazon S3", CloudProvider.AWS, "storage", "Product images and static assets", "$50-150/month", "Unlimited", ["Bucket policies", "Encryption"]),
                CloudService("CloudFront", CloudProvider.AWS, "networking", "CDN for global content delivery", "$20-100/month", "Global", ["DDoS protection", "SSL/TLS"]),
                CloudService("Application Load Balancer", CloudProvider.AWS, "networking", "Traffic distribution and SSL termination", "$30-80/month", "Auto Scaling", ["Health checks", "SSL termination"]),
                CloudService("AWS WAF", CloudProvider.AWS, "security", "Web application firewall", "$10-50/month", "Auto Scaling", ["OWASP protection", "DDoS mitigation"])
            ]
        # Similar implementations for Azure and GCP...
        return []
    
    def _design_chatbot_architecture(self, provider: CloudProvider) -> List[CloudService]:
        """Design chatbot architecture"""
        if provider == CloudProvider.AWS:
            return [
                CloudService("AWS Lambda", CloudProvider.AWS, "compute", "Serverless chatbot functions", "$50-200/month", "Auto Scaling", ["IAM roles", "VPC"]),
                CloudService("Amazon Lex", CloudProvider.AWS, "ai", "Natural language understanding", "$100-300/month", "Auto Scaling", ["Data encryption", "Access control"]),
                CloudService("Amazon DynamoDB", CloudProvider.AWS, "database", "Conversation storage", "$80-200/month", "Auto Scaling", ["Encryption at rest", "Point-in-time recovery"]),
                CloudService("Amazon API Gateway", CloudProvider.AWS, "networking", "API management", "$30-100/month", "Auto Scaling", ["API keys", "Rate limiting"]),
                CloudService("Amazon SNS", CloudProvider.AWS, "messaging", "Notifications and escalations", "$20-50/month", "Auto Scaling", ["Message encryption", "Access control"])
            ]
        return []
    
    def _design_expense_tracker_architecture(self, provider: CloudProvider) -> List[CloudService]:
        """Design expense tracker architecture"""
        if provider == CloudProvider.AWS:
            return [
                CloudService("AWS Lambda", CloudProvider.AWS, "compute", "Serverless backend API", "$50-150/month", "Auto Scaling", ["IAM roles", "VPC"]),
                CloudService("Amazon S3", CloudProvider.AWS, "storage", "Receipt image storage", "$30-100/month", "Unlimited", ["Bucket policies", "Encryption"]),
                CloudService("Amazon Textract", CloudProvider.AWS, "ai", "OCR for receipt processing", "$100-300/month", "Auto Scaling", ["Data encryption", "Access control"]),
                CloudService("Amazon RDS", CloudProvider.AWS, "database", "Expense data storage", "$80-200/month", "Read replicas", ["Encryption at rest", "VPC"]),
                CloudService("Amazon SNS", CloudProvider.AWS, "messaging", "Approval notifications", "$20-50/month", "Auto Scaling", ["Message encryption", "Access control"])
            ]
        return []
    
    def _get_deployment_strategy(self, requirements: Dict[str, Any]) -> str:
        """Determine deployment strategy"""
        if any("high_availability" in constraint for req in requirements["business_requirements"] for constraint in req.constraints):
            return "Blue-Green deployment with zero downtime"
        elif any("budget_conscious" in constraint for constraint in requirements["constraints"]):
            return "Rolling deployment with cost optimization"
        else:
            return "Canary deployment with gradual rollout"
    
    def _estimate_costs(self, services: List[CloudService]) -> str:
        """Estimate total monthly costs"""
        return "$500-1500/month depending on usage"
    
    def _get_security_considerations(self, requirements: Dict[str, Any]) -> List[str]:
        """Get security considerations"""
        considerations = ["Data encryption in transit and at rest", "Identity and access management", "Network security"]
        
        if any("PCI_DSS_compliance" in constraint for req in requirements["business_requirements"] for constraint in req.constraints):
            considerations.append("PCI DSS compliance for payment processing")
        
        if any("data_privacy" in constraint for constraint in requirements["constraints"]):
            considerations.append("GDPR compliance for data privacy")
        
        return considerations
    
    def _get_scalability_plan(self, requirements: Dict[str, Any]) -> str:
        """Get scalability plan"""
        return "Auto-scaling based on demand with horizontal scaling capabilities and load balancing"
    
    def _get_monitoring_strategy(self, requirements: Dict[str, Any]) -> str:
        """Get monitoring strategy"""
        return "Comprehensive monitoring with CloudWatch, application performance monitoring, and alerting"

class MultiAgentOrchestrator:
    """Main orchestrator for the multi-agent system"""
    
    def __init__(self):
        self.requirements_analyzer = RequirementsAnalyzer()
        self.cloud_architect = CloudArchitect()
    
    async def process_architecture_request(self, problem_description: str, preferred_provider: CloudProvider = CloudProvider.AWS) -> Dict[str, Any]:
        """Process architecture request through all agents"""
        logger.info("Starting multi-agent architecture planning process")
        
        # Step 1: Analyze requirements
        requirements = await self.requirements_analyzer.analyze_requirements(problem_description)
        
        # Step 2: Design architecture
        architecture = await self.cloud_architect.design_architecture(requirements, preferred_provider)
        
        # Compile final recommendation
        final_recommendation = {
            "problem_description": problem_description,
            "requirements": requirements,
            "architecture": architecture,
            "confidence_score": architecture.confidence_score,
            "next_steps": [
                "Review and approve architecture design",
                "Set up development environment",
                "Implement security controls",
                "Plan deployment strategy"
            ]
        }
        
        return final_recommendation

# Example usage
async def main():
    """Main function to demonstrate the multi-agent system"""
    orchestrator = MultiAgentOrchestrator()
    
    # Test scenario
    scenario = "Simple E-commerce Site - Online store for small business (1000 daily users) with product catalog, shopping cart, payment processing, and basic admin dashboard"
    
    print(f"SCENARIO: {scenario}")
    print("="*80)
    
    recommendation = await orchestrator.process_architecture_request(scenario, CloudProvider.AWS)
    
    print(f"Architecture Type: {recommendation['architecture'].architecture_type.value}")
    print(f"Confidence Score: {recommendation['confidence_score']}")
    print(f"\nRecommended Services:")
    for service in recommendation['architecture'].services:
        print(f"  - {service.name} ({service.provider.value}): {service.description}")
        print(f"    Cost: {service.cost_estimate}, Scalability: {service.scalability}")

if __name__ == "__main__":
    asyncio.run(main())

# === WRITTEN RESPONSE QUESTIONS ===

"""
QUESTION 1: AGENT DESIGN (20 points)
What agents would you create for this orchestration? Describe:
- 3-5 specific agents and their roles
- How they would collaborate on the sample problems
- What each agent's input and output would be

RESPONSE:

Agent Name: Requirements Analyzer
Role: Break down business requirements into technical needs and constraints
Input: Problem description + business context + stakeholder requirements
Output: Structured requirements (business, technical, constraints, success metrics)
Collaboration: Works first in the pipeline, provides foundation for all other agents

Agent Name: Cloud Architect
Role: Design cloud architecture based on requirements and best practices
Input: Requirements from Requirements Analyzer + cloud provider preferences
Output: Complete architecture recommendation with services, deployment strategy, costs
Collaboration: Receives requirements, coordinates with Cost Optimizer and Security Specialist

Agent Name: Cost Optimizer
Role: Analyze and optimize architecture for cost efficiency and budget constraints
Input: Architecture recommendation + budget constraints + usage patterns
Output: Cost optimization recommendations, alternative services, cost estimates
Collaboration: Reviews architecture from Cloud Architect, provides cost insights

Agent Name: Security Specialist
Role: Analyze security aspects and compliance requirements
Input: Architecture recommendation + security requirements + compliance standards
Output: Security analysis, vulnerability assessment, compliance recommendations
Collaboration: Reviews architecture from Cloud Architect, provides security insights

Agent Name: Integration Specialist
Role: Handle integration with existing systems and legacy compatibility
Input: Architecture recommendation + existing system inventory + integration requirements
Output: Integration strategy, migration plan, compatibility assessment
Collaboration: Works with Cloud Architect to ensure compatibility with existing systems

QUESTION 2: ORCHESTRATION WORKFLOW (25 points)
For ONE of the sample scenarios, walk through your complete workflow:

SCENARIO: Simple E-commerce Site

Step 1: Requirements Analysis
- Requirements Analyzer receives: "Online store for small business (1000 daily users) with product catalog, shopping cart, payment processing, basic admin dashboard"
- Output: Business requirements (scalability, security, functionality), technical requirements (web app, database, payment gateway), constraints (budget-conscious, time-to-market)

Step 2: Architecture Design
- Cloud Architect receives requirements from Step 1
- Analyzes requirements and selects appropriate cloud services
- Output: Complete architecture with EC2, RDS, S3, CloudFront, Load Balancer, WAF

Step 3: Cost Optimization
- Cost Optimizer receives architecture from Step 2
- Analyzes cost implications and suggests optimizations
- Output: Cost estimates, optimization recommendations (spot instances, auto-scaling)

Step 4: Security Analysis
- Security Specialist receives architecture from Step 2
- Analyzes security aspects and compliance needs
- Output: Security score, vulnerability assessment, PCI DSS compliance recommendations

Step 5: Integration Planning
- Integration Specialist receives architecture from Step 2
- Plans integration with existing systems
- Output: Integration strategy, migration plan, compatibility assessment

Step 6: Final Recommendation
- Orchestrator compiles all inputs into comprehensive recommendation
- Includes architecture, costs, security, integration plan, and next steps

Agent Handoffs:
- Requirements → Architecture: Structured requirements data
- Architecture → Cost/Security/Integration: Architecture recommendation
- All agents → Orchestrator: Specialized analysis results

Failure Handling:
- If Requirements Analyzer fails: Use default requirements template
- If Cloud Architect fails: Fall back to basic architecture patterns
- If any specialist fails: Continue with available analysis, flag missing components
- If Orchestrator fails: Provide individual agent outputs with manual compilation needed

Completeness Assurance:
- Validation checkpoints at each step
- Cross-agent verification of critical components
- Confidence scoring for each recommendation
- Manual review triggers for low-confidence outputs

QUESTION 3: CLOUD RESOURCE MAPPING (20 points)
For your chosen scenario, what basic cloud services would your system recommend?

COMPUTE:
- Amazon EC2: Web application servers with auto-scaling
- Justification: Handles 1000 daily users with horizontal scaling capability

STORAGE:
- Amazon RDS: MySQL/PostgreSQL database for product catalog and user data
- Justification: ACID compliance needed for e-commerce transactions
- Amazon S3: Product images and static assets
- Justification: Unlimited storage with CDN integration for global performance

NETWORKING:
- Application Load Balancer: Traffic distribution and SSL termination
- Justification: High availability and SSL security for payment processing
- CloudFront CDN: Global content delivery
- Justification: Fast image loading for better user experience

SECURITY:
- AWS WAF: Web application firewall
- Justification: Protection against OWASP Top 10 vulnerabilities
- VPC: Network isolation and security
- Justification: Secure network architecture for payment processing

MONITORING:
- CloudWatch: Application and infrastructure monitoring
- Justification: Real-time monitoring for 99.9% uptime requirement

QUESTION 4: REUSABILITY & IMPROVEMENT (15 points)
How would you make this system work across different projects?

STANDARDIZATION:
- Common agent interfaces and data structures
- Standardized requirement templates for different project types
- Common cloud service patterns and best practices
- Standardized output formats and reporting

CUSTOMIZATION:
- Project-specific requirement templates
- Custom cloud service recommendations based on project type
- Team-specific coding standards and preferences
- Industry-specific compliance requirements

LEARNING MECHANISMS:
- Feedback collection from successful deployments
- Pattern recognition from previous recommendations
- Cost optimization learning from actual usage data
- Security improvement from incident analysis

FEEDBACK LOOPS:
- Developer satisfaction surveys
- Deployment success/failure tracking
- Cost accuracy validation
- Security incident correlation
- Performance metrics collection

QUESTION 5: PRACTICAL CONSIDERATIONS (20 points)
What challenges would you expect and how would you handle:

CONFLICTING RECOMMENDATIONS:
- Implement consensus voting mechanism
- Weight recommendations by agent confidence scores
- Escalate to human review for major conflicts
- Use historical success data to break ties

INCOMPLETE/VAGUE PROBLEM STATEMENTS:
- Use requirement templates to prompt for missing information
- Implement iterative questioning to clarify requirements
- Provide default assumptions with clear documentation
- Flag uncertainty for human review

BUDGET CONSTRAINTS:
- Implement budget-aware optimization algorithms
- Provide multiple cost tiers for each recommendation
- Include cost-benefit analysis for each service
- Suggest phased implementation for budget constraints

LEGACY SYSTEM INTEGRATION:
- Maintain database of common legacy systems and integration patterns
- Provide compatibility assessment for each recommendation
- Suggest migration strategies and timelines
- Include legacy system requirements in analysis

KEEPING UP WITH NEW CLOUD SERVICES:
- Implement service discovery and evaluation pipeline
- Maintain knowledge base of new services and features
- Regular updates to service recommendations
- A/B testing of new services in non-critical environments
- Community feedback integration for service evaluation
"""