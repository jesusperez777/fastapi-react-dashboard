import { Box, Container, Text } from "@chakra-ui/react"
import { createFileRoute } from "@tanstack/react-router"
import useAuth from "@/hooks/useAuth"
import Items from "@/components/Items/Items"

export const Route = createFileRoute("/_layout/")({
  component: Dashboard,
})

function Dashboard() {
  const { user: currentUser } = useAuth()

  return (
    <Container maxW="full" pt={12}>
      <Box m={4}>
        <Text fontSize="2xl" truncate maxW="sm">
          Hi, {currentUser?.full_name || currentUser?.email} 👋🏼
        </Text>
        <Text>Welcome back, nice to see you again!</Text>
      </Box>

      {/* Mostrar los items directamente */}
      <Items />
    </Container>
  )
}
