# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import chimera_llm_pb2 as chimera__llm__pb2


class LLMStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Inspect = channel.unary_stream(
            "/LLM/Inspect",
            request_serializer=chimera__llm__pb2.InspectRequest.SerializeToString,
            response_deserializer=chimera__llm__pb2.InspectResponse.FromString,
        )
        self.LoadModel = channel.unary_unary(
            "/LLM/LoadModel",
            request_serializer=chimera__llm__pb2.LoadModelRequest.SerializeToString,
            response_deserializer=chimera__llm__pb2.LoadModelResponse.FromString,
        )
        self.Completion = channel.unary_unary(
            "/LLM/Completion",
            request_serializer=chimera__llm__pb2.CompletionRequest.SerializeToString,
            response_deserializer=chimera__llm__pb2.CompletionPrediction.FromString,
        )
        self.Chat = channel.unary_unary(
            "/LLM/Chat",
            request_serializer=chimera__llm__pb2.ChatRequest.SerializeToString,
            response_deserializer=chimera__llm__pb2.ChatPrediction.FromString,
        )


class LLMServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Inspect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def LoadModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Completion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Chat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_LLMServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Inspect": grpc.unary_stream_rpc_method_handler(
            servicer.Inspect,
            request_deserializer=chimera__llm__pb2.InspectRequest.FromString,
            response_serializer=chimera__llm__pb2.InspectResponse.SerializeToString,
        ),
        "LoadModel": grpc.unary_unary_rpc_method_handler(
            servicer.LoadModel,
            request_deserializer=chimera__llm__pb2.LoadModelRequest.FromString,
            response_serializer=chimera__llm__pb2.LoadModelResponse.SerializeToString,
        ),
        "Completion": grpc.unary_unary_rpc_method_handler(
            servicer.Completion,
            request_deserializer=chimera__llm__pb2.CompletionRequest.FromString,
            response_serializer=chimera__llm__pb2.CompletionPrediction.SerializeToString,
        ),
        "Chat": grpc.unary_unary_rpc_method_handler(
            servicer.Chat,
            request_deserializer=chimera__llm__pb2.ChatRequest.FromString,
            response_serializer=chimera__llm__pb2.ChatPrediction.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("LLM", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class LLM(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Inspect(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/LLM/Inspect",
            chimera__llm__pb2.InspectRequest.SerializeToString,
            chimera__llm__pb2.InspectResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def LoadModel(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/LLM/LoadModel",
            chimera__llm__pb2.LoadModelRequest.SerializeToString,
            chimera__llm__pb2.LoadModelResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Completion(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/LLM/Completion",
            chimera__llm__pb2.CompletionRequest.SerializeToString,
            chimera__llm__pb2.CompletionPrediction.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Chat(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/LLM/Chat",
            chimera__llm__pb2.ChatRequest.SerializeToString,
            chimera__llm__pb2.ChatPrediction.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
